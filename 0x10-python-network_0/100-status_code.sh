#!/bin/bash
# THis script sends a request to the URL passed as an argument, and displays only the status code of the response
curl -sI -o /dev/null "$1" -w "%{http_code}"
