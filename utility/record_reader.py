import json
import os

def get_records():
    players = []
    with open(os.path.join('utility', 'records.json'), "r") as jsonfile:
        data = json.load(jsonfile)
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
    keys = data.keys()
    if len(keys) > 5:
        for i in range(5):
            players += [f'{keys[i]}   {data[keys[i]]}']
    else:
        for key in keys:
            players += [f'{key}   {data[key]}']
    
    return players


print(get_records())