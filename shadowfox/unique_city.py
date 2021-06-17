import json

unq = set()
with open("sample_json.json",'r') as js:
    data = json.load(js)
    for d in data['student']:
        for k,v in d.items():
            if k == "city":
                unq.add(v)
for val in unq:
    print(val)
    print("****************")
