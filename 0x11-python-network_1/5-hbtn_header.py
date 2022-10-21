#!/usr/bin/python3
"""This takes a URL as argument, sends a request to the URL and displays the value of the
X-Request-Id variable in the header of the response"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
