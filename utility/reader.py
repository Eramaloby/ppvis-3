import json
import os

def read(file):
    with open(file, "r") as jsonfile:
        data = json.load(jsonfile)
    return data.values()

