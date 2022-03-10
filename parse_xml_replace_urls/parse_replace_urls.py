import xml.etree.ElementTree as ET
import hashlib

tree = ET.parse('ExportXML_20210712_cleanAmp.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

#start = root.find('./Objects')
start = root
print(start.tag)
print(start.attrib)
lista  = start.findall('object')
print(len(lista))
for item in lista:
    #print(item.find('{http://www.europeana.eu/schemas/edm/}isShownBy'))
    shownby_el = item.find('{http://www.europeana.eu/schemas/edm/}isShownBy')
    shownby = shownby_el.text
    print(shownby)
    base_url = "http://repos-test.europeanafashion.eu/ext2/MUDE/"
    if (shownby != None) :
        hash = hashlib.md5(shownby.encode('utf-8')).hexdigest()
        #http://repos-test.europeanafashion.eu/ext2/MUDE/a5/a5c1abd87dab09f7e21ce80e67f03a5d.jpg
        newurl = base_url + hash[:2] + '/' + hash + '.jpg'
        print(newurl)
        shownby_el.text = newurl
        #new_shownBy = ET.SubElement(item, '{http://www.europeana.eu/schemas/edm/}isShownBy')
        #new_shownBy.text = newurl
tree.write('final_output.xml')