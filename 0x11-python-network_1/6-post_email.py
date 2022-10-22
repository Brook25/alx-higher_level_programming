#!/usr/bin/python3
"""This takes a URL and an email address as arguments,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
