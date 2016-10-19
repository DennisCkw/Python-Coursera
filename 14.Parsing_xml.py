#Web Sevices Overview
# Wire format
# - Using Serialize and Deseriliaze to allow appllication to communicate with different languages
# - xml and json are just different wire formats that hold data
# - xml is better for documents, json is better for arrays
# - people use xml schema to figure out which side had the error

import xml.etree.ElementTree as ET
#ET knows how to deserialize and parse the data in python for youuuuu~

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">+1 734 303 4456</phone>
    <email hide="yes" />
</person>
'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)