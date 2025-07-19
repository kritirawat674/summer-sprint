# VALIDATE A DNA SEQUENCE

import re

sequence = input("Please input a DNA sequence: ").upper()

if re.fullmatch(r'[ATGC]+', sequence):
    print("Valid sequence:", sequence)
else:
    print("Invalid sequence. Please enter only A, T, G, or C.")