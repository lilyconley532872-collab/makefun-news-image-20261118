"""Copy the finished news image to the make.fun output directory.

The image is a single front page summing up Wednesday 18 November 2026
world news. This entrypoint does no drawing: it validates the pre-built
``entry.png`` sitting beside this file (at most 1 MiB, at most
1024x1024 pixels) and copies it byte-for-byte to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (``/output`` when the variable is
unset). A plain byte copy is deterministic, so two runs produce
identical output bytes.
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_WIDTH = 1024
MAX_HEIGHT = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_dimensions(path):
    """Return the (width, height) stored in a PNG file's IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_SIGNATURE:
        raise ValueError(f"{path}: not a PNG file (bad signature)")
    chunk_length = struct.unpack(">I", header[8:12])[0]
    chunk_type = header[12:16]
    if chunk_type != b"IHDR" or chunk_length != 13:
        raise ValueError(f"{path}: missing or malformed IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    if not os.path.isfile(source):
        raise FileNotFoundError(f"source image not found: {source}")

    size = os.path.getsize(source)
    if size > MAX_BYTES:
        raise ValueError(
            f"{source}: {size} bytes exceeds the {MAX_BYTES} byte limit"
        )

    width, height = read_png_dimensions(source)
    if width > MAX_WIDTH or height > MAX_HEIGHT:
        raise ValueError(
            f"{source}: {width}x{height} exceeds the "
            f"{MAX_WIDTH}x{MAX_HEIGHT} limit"
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")

    shutil.copyfile(source, destination)

    copied_size = os.path.getsize(destination)
    if copied_size != size:
        raise ValueError(
            f"copy size mismatch: {destination} is {copied_size} bytes, "
            f"source is {size} bytes"
        )

    print(f"Wrote {destination} ({copied_size} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
