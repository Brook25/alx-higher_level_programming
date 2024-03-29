#!/usr/bin/python3
"""takes Github credentials(u.name and passwd) as args and uses the Github API
to display id"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))
