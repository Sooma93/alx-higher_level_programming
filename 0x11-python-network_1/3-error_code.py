#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body
"""
if __name__ == "__main__":
    import sys
    from urllib import request, error

    argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as erro:
        print("Error code: {}".format(erro.status))
