import xml.etree.ElementTree as ET
nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")
root=ET.Element("persona")
nombre_element=ET.SubElement(root,"nombre")
apellido_element=ET.SubElement(root,"apellido")
nombre_element.text=nombre
apellido_element.text=apellido
cadena_xml=ET.tostring(root)
print (cadena_xml.decode())
