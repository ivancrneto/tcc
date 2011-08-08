#!/usr/bin/env python

#-*- coding:utf-8 -*-

from xml.dom import minidom

def get_a_document():
    doc = minidom.Document()
    blog_elem = doc.createElement('blog')
    doc.appendChild(blog_elem)
    
    return doc, blog_elem
    
    
def add_a_location(doc, blog_elem):
    location_elem = doc.createElement('location')
    blog_elem.appendChild(location_elem)
    
    return location_elem
    

def add_surroundings(doc, location_elem):
    surroundings_elem = doc.createElement('brasileiro-serie-a')
    location_elem.appendChild(surroundings_elem)
    description = doc.createTextNode('Descricao do surrounding: campeonato brasileiro serie a')
    surroundings_elem.appendChild(description)
    
    return surroundings_elem
    

def add_more_surroundings(doc, surroundings_elem):
    description = doc.createTextNode('Mais uma descricao: o Bahia esta na serie a!')
    surroundings_elem.appendChild(description)
    

def fix_element(elem):
    elem.normalize()
  
    
def add_building(doc, location_elem):
    building_elem = doc.createElement('building')
    location_elem.appendChild(building_elem)
    
    return building_elem
    

def name_building(building_elem):
    building_elem.setAttribute('name', 'Pituacu')
    
    
def write_to_file(doc, name='/tmp/doc.nav'):
    xml_content = doc.toxml('UTF-8')
    f = open(name, 'w')
    f.write(xml_content)
    f.close()
   
    
def get_a_document_from_path(name='/tmp/doc.nav'):
    return minidom.parse(name)
    
    
if __name__ == '__main__':
    doc, blog_elem = get_a_document()
    print doc.childNodes
    print doc.childNodes[0].namespaceURI
    print doc.childNodes[0].localName

    location_elem = add_a_location(doc, blog_elem)    
    print doc.childNodes[0].childNodes
    print doc.childNodes[0].childNodes[0]
    print doc.childNodes[0].childNodes[0].namespaceURI
    print doc.childNodes[0].childNodes[0].localName
    
    surroundings_elem = add_surroundings(doc, location_elem)
    print doc.childNodes[0].childNodes[0].childNodes[0].childNodes[0]
    print doc.childNodes[0].childNodes[0].childNodes[0].childNodes[0].nodeValue
    
    add_more_surroundings(doc, surroundings_elem)
    print surroundings_elem.childNodes
    
    fix_element(surroundings_elem)
    print doc.childNodes[0].childNodes[0].childNodes[0].childNodes[0].nodeValue
    
    building_elem = add_building(doc, location_elem)
    print location_elem.childNodes
    print location_elem.childNodes[1].namespaceURI
    
    name_building(building_elem)
    print building_elem.getAttribute('name')
    
    write_to_file(doc, '/home/ivan/Desktop/arquivo.nav')
    
    doc_read = get_a_document_from_path('/home/ivan/Desktop/arquivo.nav')
    print doc_read.childNodes[0].childNodes[0].childNodes[0].childNodes[0].nodeValue
