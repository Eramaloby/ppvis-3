import json
import os


def get(file: str, key: str):
    with open(file, "r") as configfile:
        data = json.load(configfile)
    return data[key]
