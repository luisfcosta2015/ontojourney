from __future__ import annotations

import hashlib
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[2]
OUTPUT = RELEASE_ROOT / "SHA256SUMS"


def included_files() -> list[Path]:
    return sorted(
        (
            path
            for path in RELEASE_ROOT.rglob("*")
            if path.is_file()
            and path != OUTPUT
            and "__pycache__" not in path.parts
            and path.suffix != ".pyc"
        ),
        key=lambda path: path.relative_to(RELEASE_ROOT).as_posix(),
    )


def main() -> None:
    lines = []
    for path in included_files():
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        relative = path.relative_to(RELEASE_ROOT).as_posix()
        lines.append(f"{digest}  {relative}")
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote SHA-256 checksums for {len(lines)} release files.")


if __name__ == "__main__":
    main()
