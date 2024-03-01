#!/usr/bin/python3
"""
cript that takes in a URL, sends a request to the URL
"""
if __name__ == "__main__":
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    re = post(url, {'email': email})
    print(re.text)
