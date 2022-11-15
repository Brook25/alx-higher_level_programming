#!/bin/bash
# This script checks status code and prints response body
var=$(curl -sI "$1" | head -1 | cut -d ' ' -f 2)                                             
if [ "$var" -eq 200 ]; then                                                                  
        echo $(curl -s "$1")                                                                 
fi
