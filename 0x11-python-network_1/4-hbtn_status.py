#!/usr/bin/python3
"""
cript that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    i = requests.get("https://alx-intranet.hbtn.io/status")
    j = i.text
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(j), j))
