#!/usr/bin/env python3
"""Binary diff utility that shows hex dumps in unified diff format."""
import argparse
import difflib


def hexdump(path):
    with open(path, 'rb') as f:
        data = f.read()
    lines = []
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        hex_bytes = ' '.join(f'{b:02x}' for b in chunk)
        ascii_repr = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
        lines.append(f'{i:08x}  {hex_bytes:<47}  |{ascii_repr}|')
    return lines


def main():
    parser = argparse.ArgumentParser(
        description='Show diff between two binary files as hex dumps.')
    parser.add_argument('file_a', help='First binary file')
    parser.add_argument('file_b', help='Second binary file')
    args = parser.parse_args()

    hex_a = hexdump(args.file_a)
    hex_b = hexdump(args.file_b)

    diff = difflib.unified_diff(hex_a, hex_b,
                                fromfile=args.file_a,
                                tofile=args.file_b,
                                lineterm='')
    for line in diff:
        print(line)


if __name__ == '__main__':
    main()
