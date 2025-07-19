import json

json_string = '''
{
    "experiment": "trial_5",
    "results": [
        {
            "gene": "TP53",
            "details": {
                "expression": 76,
                "mutation": false
            }
        },
        {
            "gene": "BRCA2",
            "details": {
                "expression": 45,
                "mutation": true
            }
        }
    ]
}
'''


data = json.loads(json_string)

for entry in data:
    if mutation == true:for entry in data['results']:
    if entry['details']['mutation'] == True:
        print(entry['gene'])
    print(entry['gene'])

