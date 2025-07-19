import json

json_string = '''
[
    {"gene": "TP53", "expression": 80},
    {"gene": "EGFR", "expression": 47},
    {"gene": "MYC", "expression": 95}
]
'''
data = json.loads(json_string)


for entry in data:      #since the data is a list of dictionaries, you need to loop through each dictionary(which we will call entry)
    if entry['expression'] > 70:
        print(entry['gene'])
        print(entry['expression'])
