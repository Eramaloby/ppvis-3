import json
import os

def update_records(name, wave):
    with open(os.path.join('utility', 'records.json'), "r") as jsonfile:
        data = json.load(jsonfile)
    if name in data.keys() and data[name] < wave:
        data[name] = wave
        with open(os.path.join('utility', 'records.json'), "r") as jsonfile:
            json.dump(data, jsonfile)
    elif name not in data.keys() and name != '':
        print(type(data))
        data[name] = wave
        with open(os.path.join('utility', 'records.json'), "w") as jsonfile:
            json.dump(data, jsonfile)