import json

sequence_data = ''' {
    "gene": "MYC",
    "sequence": "ATGCGTAGCTAGTACGATAGCTAGCTA"
}
'''


data = json.loads(sequence_data)

seq = data["sequence"]

nucleotide_count = {}

for base in "ATCG":
    nucleotide_count[base] = seq.count(base)

print(nucleotide_count)

gc_content = int((seq.count('G') + seq.count('C')))/len(seq)
print(gc_content)

RNA_seq = seq.replace("T", "U")
print(RNA_seq)
