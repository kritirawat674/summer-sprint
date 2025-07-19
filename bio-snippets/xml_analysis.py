import xml.etree.ElementTree as ET
import re

xml_data = '''<genes>
  <gene>
    <name>BRCA1</name>
    <sequence>ATGCGTAA</sequence>
  </gene>
  <gene>
    <name>TP53</name>
    <sequence>ATGCC12A</sequence>
  </gene>
  <gene>
    <name>EGFR</name>
    <sequence>ATGGGGCCC</sequence>
  </gene>
</genes>
'''

root = ET.fromstring(xml_data)

for gene in root.findall('gene'):
    name = gene.find('name').text
    sequence = gene.find('sequence').text
    if re.fullmatch(r'[ATGC]+', sequence):
        print(name + "" + sequence)
    else:
        print("invalid sequence " + name)

