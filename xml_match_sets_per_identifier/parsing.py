import xml.etree.ElementTree as ET

tree = ET.parse('rec1')
root = tree.getroot()

print(root.tag)
print(root.attrib)

start = root.find('./channel')
print(start.tag)
print(start.attrib)
l  = start.findall('item')
print(len(l))
res = {}
for item in start.findall('item'):
    object_number = item.find('object_number').text
#     title = item.find('title').text
#     print
#     link = item.find('link').text
#     #enclosure = item.find('enclosure')
#     #url = enclosure.get('url')
#     #print(object_number ,title,link,url)
#     #more elements exist here 
    elems = []
    for elem in item.iter():   
        elems.append(elem)
#     #    print('allvalues printed')   
    #res[object_number] = elems
    res[object_number] = item
#     res[object_number] = {'title':title,'link':link}


#print(res)


print('second xml')
tree = ET.parse('XML_2021.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

start    = root.find('./recordList')
print(start.tag)
print(start.attrib)
l  = start.findall('record')
count = 0 
print(len(l))
for item in start.findall('record'):
        object_number = item.find('object_number').text
        #print(object_number)
        link=''
        url=''
        if object_number in res: 
            count=count+1
            elem = res[object_number]
            link = elem.find('link').text
            isShownAt = ET.SubElement(item, 'isShownAt')
            isShownAt.text = link
            enclosure = elem.find('enclosure')
            if (enclosure is not None):
                url = enclosure.get('url')
                isShownBy = ET.SubElement(item,'isShownBy')
                isShownBy.text = url
                #print(url)
            #print(link)
            # for e in elem.iter():
            #     print(e.tag)
            # if elem.find('link'):
            #     link = elem.find('link').text
            #     print(link)
            # if elem.find('enclosure'):
            #     enclosure = elem.find('enclosure')
            #     url = enclosure.get('url')
            #     print(url)
            #print(object_number,link,url)


        # for every record get res[object_number] add elements

print(count)
#print(ET.tostring(start))
tree.write('final_output.xml')

#for item in start.findall('item'):