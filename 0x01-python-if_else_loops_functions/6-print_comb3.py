#!/usr/bin/python3
for num in range(0, 10):
    for num0 in range(num + 1, 10):
        if num == 8 and num0 == 9:
            print("{}{}".format(num, num0))
        else:
            print("{}{}".format(num, num0), end=", ")
