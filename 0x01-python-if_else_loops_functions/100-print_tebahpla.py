#!/usr/bin/python3
o = ""
for c in range(ord('Z'), ord('A') - 1, -1):
        o += f'{chr(c).lower()}' if (ord('z') - 
            c) % 2 == 0 else f'{chr(c)}'
        print(o, end="")
