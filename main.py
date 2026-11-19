"""Copy the finished front page to the harness output directory.

The entry image is built ahead of time and stored next to this script as
entry.png. This program only checks that the file is a complete, valid PNG
within the competition limits and then copies it byte for byte, so the
bytes the judge sees are exactly the bytes that were reviewed.

Standard library only. No network, no randomness, no clock.
"""

import os
import shutil
import struct
import sys
import zlib

SOURCE_NAME = "entry.png"
MAX_BYTES = 1048576
MAX_SIDE = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(message):
    raise SystemExit("entry check failed: " + message)


def read_png(path):
    with open(path, "rb") as handle:
        return handle.read()


def check_png(data):
    if len(data) > MAX_BYTES:
        fail("file is %d bytes, over the %d byte limit" % (len(data), MAX_BYTES))
    if len(data) < 8 or data[:8] != PNG_SIGNATURE:
        fail("missing PNG signature")
    offset = 8
    saw_header = False
    saw_end = False
    width = height = 0
    while offset < len(data):
        if offset + 8 > len(data):
            fail("truncated chunk header")
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        chunk_type = data[offset + 4:offset + 8]
        body_start = offset + 8
        body_end = body_start + length
        if body_end + 4 > len(data):
            fail("truncated chunk %r" % chunk_type)
        body = data[body_start:body_end]
        stored_crc = struct.unpack(">I", data[body_end:body_end + 4])[0]
        actual_crc = zlib.crc32(chunk_type + body) & 0xFFFFFFFF
        if stored_crc != actual_crc:
            fail("bad CRC in chunk %r" % chunk_type)
        if chunk_type == b"IHDR":
            if length != 13:
                fail("IHDR has wrong length")
            width, height = struct.unpack(">II", body[:8])
            saw_header = True
        if chunk_type == b"IEND":
            saw_end = True
            if body_end + 4 != len(data):
                fail("trailing bytes after IEND")
            break
        offset = body_end + 4
    if not saw_header:
        fail("no IHDR chunk")
    if not saw_end:
        fail("no IEND chunk")
    if width > MAX_SIDE or height > MAX_SIDE:
        fail("image is %dx%d, over the %dpx limit" % (width, height, MAX_SIDE))
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(source):
        fail("cannot find " + source)
    data = read_png(source)
    width, height = check_png(data)
    if not data:
        fail("entry.png is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, SOURCE_NAME)
    shutil.copyfile(source, target)
    copied = read_png(target)
    if copied != data:
        fail("copied file differs from entry.png")
    check_png(copied)
    print("entry.png: %dx%d, %d bytes, copied to %s" % (width, height, len(data), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
