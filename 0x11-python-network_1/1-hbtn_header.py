#!/usr/bin/python3
"""script takes URL as argument, sends a request to the URL. Displays value of
X-Request-Id variable in header of response"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
