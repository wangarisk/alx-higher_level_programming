#!/usr/bin/python3
"""Dfns a JSON file-writing fn"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON rep."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
