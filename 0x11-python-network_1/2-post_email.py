#!/usr/bin/python3
"""takes URL and email as args, sends POST request to the passed URL with the
email as parameter, and displays body of the response"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        print(response.read().decode("utf-8"))
