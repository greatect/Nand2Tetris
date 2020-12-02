import string
import xml.etree.ElementTree as ET
from functools import reduce

## Constants
COMPOSITES= ['class', 'classVarDec', 'type', 'subroutineDec', 'parameterList', \
             'subroutineBody', 'varDec', 'statements', 'letStatement', 'ifStatement', \
             'whileStatement', 'doStatement', 'returnStatement', 'expression', \
             'term', 'expressionList', 'op', 'unaryOp', 'keywordConstant']
SPEC_TERM = ['identifier', 'integerConstant', 'stringConstant']
SEQ       = 1
TEST_SEQ  = 2
UNT       = 3
TEST_UNT  = 4
TEST_UNC  = 5

## Global variables
class TokenList:
  def __init__(self):
    self.tokens = []
    self.tokend = 0
T = TokenList()

def Expect(node, case, *args):
  global T
  ## print(T.tokens[T.tokend].text)
  if case in [SEQ, TEST_SEQ]: ## args as sequential terminal/composites
    for i,arg in enumerate(args):
      if arg in COMPOSITES:
        try:
          SyntaxAnalyzer(node, arg)
        except Exception as err:
          if case == TEST_SEQ and i == 0: return 0
          raise err
      elif arg in SPEC_TERM:
        if not (T.tokend < len(T.tokens) and T.tokens[T.tokend].tag == arg):
          if case == TEST_SEQ and i == 0: return 0
          raise Exception("expecting '%s'" % arg)
        node.append(T.tokens[T.tokend])
        T.tokend += 1
      else:
        cond = T.tokend < len(T.tokens) and (T.tokens[T.tokend].text.strip() == arg)
        if not cond:
          if case == TEST_SEQ and i == 0: return 0
          raise Exception("expecting '%s'" % arg)
        node.append(T.tokens[T.tokend])
        T.tokend += 1
  elif case in [UNT, TEST_UNT]: ## args as union terminals
    allow_id = reduce(lambda x, y: x or y, [z in args for z in SPEC_TERM], False)
    cond1 = allow_id and T.tokend < len(T.tokens) and T.tokens[T.tokend].tag in SPEC_TERM
    cond2 = T.tokend < len(T.tokens) and T.tokens[T.tokend].text.strip() in args
    if not (cond1 or cond2):
      if case == TEST_UNT: return 0
      raise "expecting '%s'" % ('/'.join(args + (tuple('identifier') if allow_id else [])))
    node.append(T.tokens[T.tokend])
    T.tokend += 1
  elif case == TEST_UNC: ## args as union composites
    for arg in args:
      if Expect(node, TEST_SEQ, arg): return 1
    return 0
  return 1

def SyntaxAnalyzer(parent, attribute):
  global T
  node = ET.Element(attribute)
  if attribute == 'class':
    Expect(node, UNT, 'class') ## special
    Expect(node, SEQ, 'identifier', '{')
    while Expect(node, TEST_UNC, 'classVarDec', 'subroutineDec'): pass
    Expect(node, SEQ, '}')
  if attribute == 'classVarDec':
    Expect(node, UNT, 'static', 'field')
    Expect(node, SEQ, 'type', 'identifier')
    while Expect(node, TEST_SEQ, ',', 'identifier'): pass
    Expect(node, SEQ, ';')
  if attribute == 'type':
    Expect(parent, UNT, 'int', 'char', 'boolean', 'identifier')
  if attribute == 'subroutineDec':
    Expect(node, UNT, 'constructor', 'function', 'method')
    Expect(node, UNT, 'void', 'int', 'char', 'boolean', 'identifier')
    Expect(node, SEQ, 'identifier', '(', 'parameterList', ')', 'subroutineBody')
  if attribute == 'parameterList':
    if Expect(node, TEST_SEQ, 'type', 'identifier'):
      while Expect(node, TEST_SEQ, ',', 'type', 'identifier'): pass
  if attribute == 'subroutineBody':
    Expect(node, SEQ, '{')
    while Expect(node, TEST_SEQ, 'varDec'): pass
    Expect(node, SEQ, 'statements', '}')
  if attribute == 'varDec':
    Expect(node, SEQ, 'var', 'type', 'identifier')
    while Expect(node, TEST_SEQ, ',', 'identifier'): pass
    Expect(node, SEQ, ';')
  if attribute == 'statements':
    while Expect(node, TEST_UNC, 'letStatement', 'ifStatement', \
            'whileStatement', 'doStatement', 'returnStatement'): pass
  if attribute == 'letStatement':
    Expect(node, SEQ, 'let', 'identifier')
    Expect(node, TEST_SEQ, '[', 'expression', ']')
    Expect(node, SEQ, '=', 'expression', ';')
  if attribute == 'ifStatement':
    Expect(node, SEQ, 'if', '(', 'expression', ')', '{', 'statements', '}')
    Expect(node, TEST_SEQ, 'else', '{', 'statements', '}')
  if attribute == 'whileStatement':
    Expect(node, SEQ, 'while', '(', 'expression', ')', '{', 'statements', '}')
  if attribute == 'doStatement':
    Expect(node, SEQ, 'do', 'identifier')
    Expect(node, TEST_SEQ, '.', 'identifier')
    Expect(node, SEQ, '(', 'expressionList', ')', ';')
  if attribute == 'returnStatement':
    Expect(node, SEQ, 'return')
    Expect(node, TEST_SEQ, 'expression')
    Expect(node, SEQ, ';')
  if attribute == 'expression':
    Expect(node, SEQ, 'term')
    while Expect(node, TEST_SEQ, 'op', 'term'): pass
  if attribute == 'term':
    if not Expect(node, TEST_UNC, 'integerConstant', 'stringConstant', 'keywordConstant'):
      if not Expect(node, TEST_SEQ, '(', 'expression', ')'):
        if not Expect(node, TEST_SEQ, 'unaryOp', 'term'):
          if Expect(node, TEST_SEQ, 'identifier'):
            if not Expect(node, TEST_SEQ, '[', 'expression', ']'):
              # maybe a subroutineCall or not
              Expect(node, TEST_SEQ, '.', 'identifier')
              Expect(node, TEST_SEQ, '(', 'expressionList', ')')
          else:
            raise Exception('expecting a term')
  if attribute == 'expressionList':
    if Expect(node, TEST_SEQ, 'expression'):
      while Expect(node, TEST_SEQ, ',', 'expression'): pass
  if attribute == 'op':
    Expect(parent, UNT, '+', '-', '*', '/', '&', '|', '<', '>', '=')
  if attribute == 'unaryOp':
    Expect(parent, UNT, '-', '~')
  if attribute == 'keywordConstant':
    Expect(parent, UNT, 'true', 'false', 'null', 'this')
  ## Append to parent
  if attribute not in ['type', 'op', 'unaryOp', 'keywordConstant']:
    parent.append(node)
  return

