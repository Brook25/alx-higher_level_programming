#!/bin/bash
# This script takes a URL and sends a POST request to the passed URL, and displays the body of the response
curl -s "$1" -d email=test@gmail.com -d subject='I will always be here for PLD'
