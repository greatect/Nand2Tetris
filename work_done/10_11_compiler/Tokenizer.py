import string
from Xmlutil import make_node

## Constants
TERMINALS = ['keyword', 'symbol', 'integerConstant', 'stringConstant', 'identifier']
KEYWORDS  = ['class', 'constructor', 'function', 'method', 'field', 'static', 
            'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null',
            'this', 'let', 'do', 'if', 'else', 'while', 'return']
SYMBOLS   = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-',
            '*', '/', '&', '|', '<', '>', '=', '~']
DIGITS    = string.digits
LETTERS   = string.ascii_letters + string.digits + '_'

def Tokenizer(text):
  ## Remove comments
  while text.find('/*') != -1:
    offset = text.find('/*')
    endpos = text.find('*/', offset+2)
    assert endpos != -1, \
           'comment in line %d not closed' % (text[:offset].count('\n') + 1)
    if endpos == -2: text = text[:offset]
    else: text = text[:offset] + '\n' + text[endpos+2:]
  while text.find('//') != -1:
    offset = text.find('//')
    endpos = text.find('\n', offset+2)
    text = text[:offset] + text[endpos:]
  ## Deal with strings
  list_strings = []
  offset = 0
  while text.find('"', offset) != -1:
    offset = text.find('"', offset)
    endpos = text.find('"', offset+1)
    linepos= text.find('\n', offset+1)
    assert (endpos != -1) and ((endpos < linepos) or (linepos == -1)), \
           'string in line %d not closed' % (text[:offset].count('\n') + 1)
    list_strings.append( text[offset+1:endpos] )
    text = text[:offset] + text[endpos:]
    offset += 1
  offset = 0
  ## split tokens
  for symbol in SYMBOLS:
    text = text.replace(symbol, ' ' + symbol + ' ')
  text = text.split()
  ## label tokens
  ret = []
  for lex in text:
    if lex in KEYWORDS:
      ret += make_node(lex, TERMINALS[0])
    elif lex in SYMBOLS:
      ret += make_node(lex, TERMINALS[1])
    elif lex[0] in DIGITS:
      for d in lex:
        assert (d in DIGITS), "invalid number %s" % lex
      ret += make_node(lex, TERMINALS[2])
    elif lex == '"':
      ret += make_node(list_strings[offset], TERMINALS[3])
      offset += 1
    elif lex[0] in LETTERS:
      for d in lex:
        assert (d in LETTERS), "invalid identifier %s" % lex
      ret += make_node(lex, TERMINALS[4])
    else:
      raise Exception("unknown token %s", lex)
  return ret

