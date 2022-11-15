#!/bin/bash
# This script takes a URL and displays all HTTP methods the server will accept
curl -sI OPTIONS "$1" | grep "Allow" | cut -d' ' -f 2-
