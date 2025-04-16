#!/usr/bin/env python3
import glob
import json
import sys

def read_files(paths):
    """Read files and return a list of dictionaries with filename and contents."""
    files = []
    for path in paths:
        for filepath in glob.glob(path):
            try:
                with open(filepath, 'r') as file:
                    contents = file.read()
                    files.append({
                        "filename": filepath,
                        "contents": contents
                    })
            except Exception as e:
                print(f"Error reading file {filepath}: {str(e)}", file=sys.stderr)
                sys.exit(1)
    return files

def main():
    if len(sys.argv) < 2:
        print("Usage: python program.py <path1> [<path2> ...]", file=sys.stderr)
        sys.exit(1)

    paths = sys.argv[1:]
    files = read_files(paths)

    # Output JSON to stdout
    json.dump(files, sys.stdout, indent=2)

if __name__ == "__main__":
    main()
