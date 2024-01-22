#!/usr/bin/env python3

from path import Path

def main():
    try:
        Path.makedirs('something')
    except FileExistsError as e:
        print(f'Error: {e}')
    Path.touch('something/file.txt')
    f = Path('something/file.txt')
    f.write_text('Hello Something!')
    print(f.read_text())

if __name__ == '__main__':
    main()