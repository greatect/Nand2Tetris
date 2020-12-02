import xml.etree.ElementTree as ET

class SymbolTable:
  def __init__(self):
    self.mapping = {}
    self.count = {'static':0, 'field':0, 'argument':0, 'local':0}
  def define(self, _kind, _type, _name):
    if _name in self.mapping: raise Exception('redefinition of symbol %s' % _name)
    if _kind not in self.count: raise Exception('unknown variable attribute %s' % _kind)
    _index = self.count[_kind]
    self.count[_kind] += 1
    self.mapping[_name] = (_kind, _type, _index)
  def lookup(self, _name):
    if _name not in self.mapping: return None
    return self.mapping[_name]
  def access(info, op):
    assert op in ['push', 'pop'], 'Invalid operation'
    _kind, _, _index = info
    if _kind == 'field': _kind = 'this'
    return ['%s %s %d' % (op, _kind, _index)]

class VM:
  def __init__(self):
    self.code = []

class_name     = None
class_symbol   = None
class_memory   = 0
class_methods  = []
routine_symbol = None
function_name  = None
function_sig   = {}
function_ret   = {}
cond_label_cnt = 0
vm = VM()

def CodeWriter(node):
  global class_name, function_name, class_symbol, routine_symbol
  global class_memory, class_methods
  global function_sig, function_ret, cond_label_cnt, vm
  """
  print(node.tag, end=': ')
  for subnode in node:
    print(subnode.text, end=', ')
  print('\\')
  """
  if node.tag == 'class':
    class_name = node[1].text
    class_symbol = SymbolTable()
    class_memory = 0
    class_methods = []
    for i in range(3, len(node)-1):
      if node[i].tag == 'classVarDec': class_memory += CodeWriter(node[i])
    for i in range(3, len(node)-1):
      if node[i].tag == 'subroutineDec' and node[i][0].text == 'method':
        class_methods += [node[i][2].text]
    for i in range(3, len(node)-1):
      if node[i].tag == 'subroutineDec': CodeWriter(node[i])
    return

  elif node.tag == 'classVarDec':
    _kind = node[0].text
    _type = node[1].text
    for i in range(2, len(node), 2):
      class_symbol.define(_kind, _type, node[i].text)
    return (len(node) - 2) // 2

  elif node.tag == 'subroutineDec':
    routine_symbol = SymbolTable()
    pre_sig = [node[1].text]
    need_alloc = False
    is_method = False
    if node[0].text == 'constructor':
      if node[2].text != 'new':
        raise Exception('the name of the constructor in class %s must be "new"' % class_name)
      need_alloc = True
    elif node[0].text == 'method':
      routine_symbol.define('argument', class_name, 'this')
      pre_sig.append(class_name)
      is_method = True
    function_name = class_name + '.' + node[2].text
    function_sig[ function_name ] = tuple( pre_sig + CodeWriter(node[4]) )
    node = node[6]
    function_memory = 0
    for i in range(1, len(node)-2):
      function_memory += CodeWriter(node[i])
    vm.code += ['function %s %d' % (function_name, function_memory)]
    if need_alloc:
      vm.code += ['push constant %d' % class_memory, 'call Memory.alloc 1', 'pop pointer 0']
    if is_method:
      vm.code += ['push argument 0', 'pop pointer 0']
    cond_label_cnt = 1
    CodeWriter(node[-2])

  elif node.tag == 'parameterList':
    sig = []
    for i in range(0, len(node), 3):
      if class_symbol.lookup(node[i+1].text) != None:
        raise Exception('declaration of argument %s is an existing variable'% node[i+1].text)
      routine_symbol.define('argument', node[i].text, node[i+1].text)
      sig.append(node[i].text)
    return sig
  
  elif node.tag == 'varDec':
    _type = node[1].text
    for i in range(2, len(node), 2):
      if class_symbol.lookup(node[i].text) != None:
        raise Exception('declaration of local variable %s is an existing variable'% node[i].text)
      routine_symbol.define('local', _type, node[i].text)
    return (len(node) - 2) // 2
  
  elif node.tag == 'statements':
    for i in range(len(node)): CodeWriter(node[i])

  elif node.tag == 'letStatement':
    CodeWriter(node[-2])
    info = routine_symbol.lookup(node[1].text)
    if info == None: info = class_symbol.lookup(node[1].text)
    if info == None: raise Exception('variable %s undefined' % node[1].text)
    if node[2].text == '[':
      vm.code += SymbolTable.access(info, 'push')
      CodeWriter(node[3])
      vm.code += ['add', 'pop pointer 1', 'pop that 0']
    else:
      vm.code += SymbolTable.access(info, 'pop')

  elif node.tag == 'ifStatement':
    label_1 = function_name + '::' + str(cond_label_cnt) + 'A'
    label_2 = function_name + '::' + str(cond_label_cnt) + 'B'
    cond_label_cnt += 1
    CodeWriter(node[2])
    vm.code += ['not', 'if-goto %s' % label_1]
    CodeWriter(node[5])
    if len(node) > 7:
      vm.code += ['goto %s' % label_2, 'label %s' % label_1]
      CodeWriter(node[9])
      vm.code += ['label %s' % label_2]
    else:
      vm.code += ['label %s' % label_1]

  elif node.tag == 'whileStatement':
    label_1 = function_name + '::' + str(cond_label_cnt) + 'A'
    label_2 = function_name + '::' + str(cond_label_cnt) + 'B'
    cond_label_cnt += 1
    vm.code += ['label %s' % label_1]
    CodeWriter(node[2])
    vm.code += ['not', 'if-goto %s' % label_2]
    CodeWriter(node[5])
    vm.code += ['goto %s' % label_1, 'label %s' % label_2]

  elif node.tag == 'doStatement':
    apply_num_param = 0
    if node[2].text == '.':
      info = routine_symbol.lookup(node[1].text)
      if info == None: info = class_symbol.lookup(node[1].text)
      if info != None:
        vm.code += SymbolTable.access(info, 'push')
        apply_num_param = 1
        apply_func = info[1] + '.' + node[3].text
      else:
        apply_func = node[1].text + '.' + node[3].text
    else:
      apply_func = class_name + '.' + node[1].text
      if node[1].text in class_methods:
        vm.code += ['push pointer 0']
        apply_num_param += 1
    CodeWriter(node[-3])
    apply_num_param += (len(node[-3]) + 1) // 2
    vm.code += ['call %s %d' % (apply_func, apply_num_param), 'pop temp 0']

  elif node.tag == 'returnStatement':
    if node[1].tag == 'expression':
      assert (function_sig[function_name][0] != 'void'), '%s should not have return values' % function_name
      CodeWriter(node[1])
    else:
      assert (function_sig[function_name][0] == 'void'), '%s returned without return value' % function_name
      vm.code += ['push constant 0']
    vm.code += ['return']

  elif node.tag == 'expressionList':
    for i in range(0, len(node), 2):
      CodeWriter(node[i])

  elif node.tag == 'expression':
    operator = {'+':'add', '-':'sub', '&':'and', '|':'or', '<':'lt', '>':'gt', '=':'eq'}
    operator['*'] = 'call Math.multiply 2'
    operator['/'] = 'call Math.divide 2'
    CodeWriter(node[0])
    for i in range(1, len(node), 2):
      CodeWriter(node[i+1])
      if node[i].text not in operator:
        raise Exception('undefined binary operator %s' % node[i].text)
      vm.code += [operator[node[i].text]]

  elif node.tag == 'term':
    if node[0].tag == 'integerConstant':
      vm.code += ['push constant %s' % node[0].text]
    elif node[0].tag == 'keyword':
      if node[0].text in ['true', 'false', 'null']:
        vm.code += ['push constant 0']
        if node[0].text == 'true': vm.code += ['not']
      elif node[0].text == 'this':
        try: vm.code += ['push pointer 0']
        except: raise Exception('"this" is not defined in function %s' % function_name)
      else:
        raise Exception('undefined keyword term %s' % node[0].text)
    elif node[0].tag == 'stringConstant':
      vm.code += ['push constant %d' % len(node[0].text), 'call String.new 1']
      for char in node[0].text:
        vm.code += ['push constant %d' % ord(char), 'call String.appendChar 2']
    elif node[0].text == '(':
      CodeWriter(node[1])
    elif node[0].tag == 'symbol':
      operator = {'-':'neg', '~':'not'}
      if node[0].text not in operator:
        raise Exception('undefined unary operator %s' % node[0].text)
      CodeWriter(node[1])
      vm.code += [operator[node[0].text]]
    else:
      info = routine_symbol.lookup(node[0].text)
      if info == None: info = class_symbol.lookup(node[0].text)
      if info == None:
        apply_num_param = 0
        if node[-1].text != ')':
          raise Exception('undefined variable %s' % node[0].text)
        if node[1].text == '.':
          apply_func = node[0].text + '.' + node[2].text
        else:
          apply_func = class_name + '.' + node[0].text
          if node[1].text in class_methods:
            vm.code += ['push pointer 0']
            apply_num_param = 1
        CodeWriter(node[-2])
        apply_num_param += (len(node[-2]) + 1) // 2
        vm.code += ['call %s %d' % (apply_func, apply_num_param)]
      else:
        vm.code += SymbolTable.access(info, 'push')
        if len(node) > 1 and node[1].text == '[':
          CodeWriter(node[2])
          vm.code += ['add', 'pop pointer 1', 'push that 0']
        elif len(node) > 1 and node[1].text == '.':
          CodeWriter(node[-2])
          apply_num_param = (len(node[-2]) + 1) // 2 + 1
          apply_func = info[1] + '.' + node[2].text
          vm.code += ['call %s %d' % (apply_func, apply_num_param)]
  else:
    raise Exception('unknown tag %s\n' % node.tag)

