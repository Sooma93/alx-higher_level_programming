#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST
"""
if __name__ == "__main__":
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    re = post(url, {"email": email})
    print(re.text)
