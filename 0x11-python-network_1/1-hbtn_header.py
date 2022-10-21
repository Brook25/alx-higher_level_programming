#!/usr/bin/python3
"""Thist script takes a URL as argument, sends a request to the URL and displays the value of the
X-Request-Id variable in the header of the response"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
