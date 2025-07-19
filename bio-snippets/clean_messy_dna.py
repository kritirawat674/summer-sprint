#CLEAN A MESSY TEXT FOR DNA SEQUENCE

import re

sequences = {}
sequences["Patient_1"] = "AGGT--TAGC"
sequences["Patient_2"] = "ATGC123GAT"
 
for patient, sequence in sequences.items():
    sequence_clean= re.findall(r'[ATGC]+', sequence)
    print(sequence_clean)
