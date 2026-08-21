from __future__ import annotations

from hashlib import sha256
from pathlib import Path, PurePosixPath
import shutil
import zipfile


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = ROOT / "ontology"
PUBLIC = ROOT / "public"
VERSION = "0.9.1"
PACKAGE_NAME = f"ontojourney-core-v{VERSION}"
OUT = PUBLIC / "artifacts" / VERSION
ARCHIVE_NAME = f"{PACKAGE_NAME}.zip"
ARCHIVE_TIMESTAMP = (2026, 8, 21, 0, 0, 0)


def digest(path: Path) -> str:
    result = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def package_files(root: Path) -> list[Path]:
    return sorted(
        (path for path in root.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(root).as_posix(),
    )


def verify_manifest(root: Path) -> int:
    manifest = root / "SHA256SUMS"
    if not manifest.is_file():
        raise FileNotFoundError(f"Missing checksum manifest: {manifest}")

    entries: dict[str, str] = {}
    for line_number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            checksum, relative = line.split(None, 1)
        except ValueError as error:
            raise ValueError(f"Malformed SHA256SUMS line {line_number}: {line!r}") from error

        relative = relative.strip()
        posix_path = PurePosixPath(relative)
        if (
            len(checksum) != 64
            or any(character not in "0123456789abcdef" for character in checksum)
            or posix_path.is_absolute()
            or relative in {"", "."}
            or ".." in posix_path.parts
        ):
            raise ValueError(f"Unsafe or malformed SHA256SUMS line {line_number}: {line!r}")
        if relative in entries:
            raise ValueError(f"Duplicate checksum entry: {relative}")
        entries[relative] = checksum

    expected = {
        path.relative_to(root).as_posix()
        for path in package_files(root)
        if path != manifest
    }
    listed = set(entries)
    if listed != expected:
        missing = sorted(expected - listed)
        unlisted = sorted(listed - expected)
        raise ValueError(
            "Checksum manifest does not cover the package exactly: "
            f"missing entries={missing}; nonexistent entries={unlisted}"
        )

    for relative, checksum in entries.items():
        path = root / Path(relative)
        actual = digest(path)
        if actual != checksum:
            raise ValueError(
                f"Checksum mismatch for {relative}: expected {checksum}, found {actual}"
            )
    return len(entries)


def write_archive(source: Path, archive: Path) -> int:
    files = package_files(source)
    with zipfile.ZipFile(
        archive,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as bundle:
        for path in files:
            relative = path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(
                filename=f"{PACKAGE_NAME}/{relative}",
                date_time=ARCHIVE_TIMESTAMP,
            )
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.flag_bits |= 0x800
            bundle.writestr(
                info,
                path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
    return len(files)


def verify_archive(source: Path, archive: Path) -> None:
    expected = {
        f"{PACKAGE_NAME}/{path.relative_to(source).as_posix()}": path
        for path in package_files(source)
    }
    with zipfile.ZipFile(archive) as bundle:
        if bundle.testzip() is not None:
            raise ValueError(f"Archive integrity check failed: {archive}")
        names = set(bundle.namelist())
        if names != set(expected):
            raise ValueError("Archive entries do not match the release package")
        for name, path in expected.items():
            if bundle.read(name) != path.read_bytes():
                raise ValueError(f"Archive content differs for {name}")


def main() -> None:
    source_entries = verify_manifest(ONTOLOGY)

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ONTOLOGY, OUT)
    verify_manifest(OUT)

    archive = OUT / ARCHIVE_NAME
    archived_files = write_archive(ONTOLOGY, archive)
    verify_archive(ONTOLOGY, archive)

    with (OUT / "SHA256SUMS").open("a", encoding="utf-8") as stream:
        stream.write(f"{digest(archive)}  {ARCHIVE_NAME}\n")
    public_entries = verify_manifest(OUT)

    print(
        f"Published {source_entries} checksummed files plus SHA256SUMS; "
        f"archived {archived_files} files."
    )
    print(f"Archive: {archive}")
    print(f"Public manifest entries: {public_entries}")


if __name__ == "__main__":
    main()
