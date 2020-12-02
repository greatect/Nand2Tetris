import sys
import os
import copy
import xml.etree.ElementTree as ET
from Xmlutil import indent
from Tokenizer import Tokenizer
from SyntaxAnalyzer import SyntaxAnalyzer, T
from CodeWriter import CodeWriter, vm

def Compiler(path):
  global T, vm
  if os.path.isfile(path) and path[-5:] == '.jack':
    sys.stderr.write("Compiling Jack file %s\n" % path)
    try:
      f = open(path)
    except:
      sys.stderr.write("(Error) Cannot open file %s\n" % path)
      return 1
    try:
      T.tokens = Tokenizer(f.read())
      T.tokend = 0
      f.close()
    except Exception as err:
      sys.stderr.write("(Error) Tokenization failed: %s\n" % str(err))
      return 1
    try:
      root = ET.Element('SyntaxLayout')
      SyntaxAnalyzer(root, 'class')
    except Exception as err:
      sys.stderr.write("(Error) Invalid syntax: %s\n" % str(err))
      return 1
    try:
      path_xml = path[:-5] + '.xml'
      pretty_xml = copy.deepcopy(root[0])
      indent(pretty_xml)
      ET.ElementTree(pretty_xml).write(path_xml)
    except:
      sys.stderr.write("(Error) Cannot write to file %s\n" % path_xml)
    try:
      vm.code = []
      CodeWriter(root[0])
    except Exception as err:
      sys.stderr.write("(Error) Invalid syntax: %s\n" % str(err))
    try:
      path = path[:-5] + '.vm'
      f = open(path, 'w')
      f.write('\n'.join(vm.code) + '\n')
      f.close()
    except:
      sys.stderr.write("(Error) Cannot write to file %s\n" % path)
    return 1
  num_jack = 0
  if os.path.isdir(path):
    for filename in os.listdir(path):
      num_jack += Compiler(path + '/' + filename)
  return num_jack

if __name__ == '__main__':
  assert len(sys.argv) > 1, "Error: require a directory or a single jack file as argument"
  assert Compiler(sys.argv[1]) > 0, "Error: no jack files were found"

