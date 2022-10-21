#!/usr/bin/python3
"""takes URL as arg, sends request to the URL and displays the value of the
X-Request-Id variable in header of the response"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
