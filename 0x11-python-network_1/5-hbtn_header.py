#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    re = get(argv[1])
    print(re.headers.get("X-Request-Id"))
