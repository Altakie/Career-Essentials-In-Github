import yaml
import xml.etree.ElementTree as xml_tree

with open('doc.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    xml_element = xml_tree.Element('xml')

link_prefix = yaml_data['link']

xml_tree.SubElement(xml_element, 'title').text = yaml_data['title']
xml_tree.SubElement(xml_element, 'image', {'href' : link_prefix + yaml_data['image']}) 
body = xml_tree.SubElement(xml_element, 'body')


for item in yaml_data['item']:
    item_element = xml_tree.SubElement(body, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(item_element, 'description').text = item['description']
    xml_tree.SubElement(item_element, 'image', {'href' : link_prefix + item['image']})





output_tree = xml_tree.ElementTree(xml_element)
output_tree.write('doc.xml', encoding='UTF-8', xml_declaration=True)