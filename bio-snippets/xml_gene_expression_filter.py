import xml.etree.ElementTree as ET

xml_data = ''' <experiments>
  <gene>
    <name>BRCA1</name>
    <expression>87</expression>
  </gene>
  <gene>
    <name>TP53</name>
    <expression>42</expression>
  </gene>
  <gene>
    <name>EGFR</name>
    <expression>93</expression>
  </gene>
</experiments>
'''
root = ET.fromstring(xml_data)

for gene in root.findall('gene'):
    name = gene.find('name').text
    expression = gene.find('expression').text
        if int(expression) > 80:
            print(name + "" + str(expression))
