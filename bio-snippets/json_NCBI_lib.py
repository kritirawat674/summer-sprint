import urllib.request
import json

gene_id = input("enter gene id: ")

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=" + gene_id + "&retmode=json"

response = urllib.request.urlopen(url)
raw_data = response.read().decode()

data = json.loads(raw_data)

print(json.dumps(data,indent=4))  #used this only to find out the hierarchy of data and if its in dictionary or list, etc, can remove it later

gene_name = data["result"]["672"]["name"]
print(gene_name)
