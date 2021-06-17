import json

with open("sample_json.json",'r') as js:
    data = json.load(js)
    for d in data['student']:
        for k,v in d.items():
            print(k,":",v)
        print("****************")