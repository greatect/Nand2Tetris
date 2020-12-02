import xml.etree.ElementTree as ET

def make_node(text, tag):
  ret = ET.Element(tag)
  ret.text = text
  return [ret]

def indent(elem, level=0, noindent=False):
  spaces = "" if noindent else "  "
  i = "\n" + level * spaces
  if elem.text:
    elem.text = ' ' + elem.text + ' '
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + spaces
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      indent(elem, level+1, noindent)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i

