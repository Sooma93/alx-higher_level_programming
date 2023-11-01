#!/usr/bin/python3
for c in range(ord('Z'), ord('A') - 1, -1):
        print(f'{chr(c).lower()}' if (ord('z') - c) % 2 == 0 else
                f'{chr(c)}', end='')
