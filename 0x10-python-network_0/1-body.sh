#!/bin/bash
# This script takes a URL, sends GET request to the URL, and displays the body of the response
curl -s "$1" -X GET -L 
