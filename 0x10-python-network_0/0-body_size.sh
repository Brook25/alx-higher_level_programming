#!/bin/bash
# This script takes a URL, sends a request to the URL, and displays the size of the body of the response
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
