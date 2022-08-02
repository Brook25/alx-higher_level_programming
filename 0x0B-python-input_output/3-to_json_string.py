#!/usr/bin/python3
""" Program writes an object to a Text file using JSON representation"""
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string) """
    return (json.dumps(my_obj))
