import sys
import os
import string

symbol_record = {}
static_base = 16
def mark(word, assign=False, disable_check=False):
  global symbol_record
  mask = 0b10 if assign==True else 0b01
  if not disable_check:
    ascii_symbol = string.ascii_letters + string.digits + "_:."
    for x in word: 
      assert (x in ascii_symbol), 'Syntax Error of label %s' % word
    if ':' in word:
      assert (word[word.find(':')+1] not in string.digits), 'Syntax Error of label %s' % word
    elif '.' in word:
      assert (word.split('.')[-1][0] not in string.digits), 'Syntax Error of label %s' % word
  if word not in symbol_record:
    symbol_record[ word ] = 0
  assert (symbol_record[ word ] & 0b10 != mask), 'Repeated declaration of label %s' % word
  symbol_record[ word ] |= mask
  if assign:
    return '( ' + word + ' )'
  return '@ ' + word

def get_initial_code():
  return ['@ 256', 'D=A', '@ SP', 'M=D'] + translate('call Sys.init 0', '_STARTUP')

def translate(text, scope):
  global static_base
  binary_arith = {'add':'M=M+D', 'sub':'M=M-D', 'and':'M=M&D', 'or':'M=M|D'}
  binary_logic = {'eq':'D;JEQ', 'gt':'D;JGT', 'lt':'D;JLT'}
  unary_arith = {'neg':'M=-M', 'not':'M=!M'}
  segment_A = {'pointer': 'R3', 'temp': 'R5'}
  segment_B = {'local': 'LCL', 'argument': 'ARG', 'this': 'THIS', 'that': 'THAT'}

  code = []
  lines = list(map(lambda x: x.split('//')[0].strip(), text.split('\n')))
  lines = list(filter(None, lines))
  curr_funcname = scope
  count_logic = 0
  static_usage = static_base
  for i, line in enumerate(lines):
    words = line.split()

    # Arithmetic / Logic
    if words[0] in binary_arith:
      assert len(words)==1, "Syntax Error at %s" % line
      code += ['@ SP','M=M-1','A=M','D=M','A=A-1', binary_arith[words[0]] ]
    elif words[0] in unary_arith:
      assert len(words)==1, "Syntax Error at %s" % line
      code += ['@ SP','A=M-1', unary_arith[words[0]] ]
    elif words[0] in binary_logic:
      assert len(words)==1, "Syntax Error at %s" % line
      code += ['@ SP','M=M-1','A=M','D=M','A=A-1', 'D=M-D', 'M=-1']
      addr = '$LOGIC_' + curr_funcname + ':' + str(count_logic)
      count_logic += 1
      code += ['@ '+addr, binary_logic[words[0]],'@ SP','A=M-1','M=0', '('+addr+')']

    # Stack operation
    elif words[0] == 'push' or words[0] == 'pop':
      assert len(words)==3, "Syntax Error at %s" % line
      for x in words[2]:
        assert x in string.digits, "Syntax Error at %s" % line
      if words[1] == 'constant':
        code += ['@ '+words[2], 'D=A', '@ SP', 'A=M', 'M=D', '@ SP', 'M=M+1']
      elif words[1] == 'static':
        addr = static_base + int(words[2], 10)
        assert (addr < 256), 'Using too much static variables'
        code += ['D=0', '@ '+str(addr)]
        static_usage = max(static_usage, addr)
      elif words[1] in segment_A:
        code += ['@ '+segment_A[words[1]], 'D=A', '@ '+words[2]]
      elif words[1] in segment_B:
        code += ['@ '+segment_B[words[1]], 'D=M', '@ '+words[2]]
      else:
        raise Exception("Syntax Error at %s" % line)
      if words[0] == 'push' and words[1] != 'constant':
        code += ['A=D+A', 'D=M', '@ SP', 'A=M', 'M=D', '@ SP', 'M=M+1']
      elif words[0] == 'pop':
        code += ['D=D+A', '@ SP', 'M=M-1', 'A=M+1', 'M=D', 'A=A-1', 'D=M', 'A=A+1', 'A=M', 'M=D']

    # Flow control
    elif words[0] == 'label':
      assert len(words)==2, "Syntax Error at %s" % line
      code += [ mark(curr_funcname + ':' + words[1], assign=True) ]
    elif words[0] == 'goto':
      assert len(words)==2, "Syntax Error at %s" % line
      code += [ mark(curr_funcname + ':' + words[1]), '0;JMP']
    elif words[0] == 'if-goto':
      assert len(words)==2, "Syntax Error at %s" % line
      code += ['@ SP', 'M=M-1', 'A=M', 'D=M']
      code += [ mark(curr_funcname + ':' + words[1]), 'D;JNE']

    # Subroutine call
    elif words[0] == 'function':
      assert len(words)==3, "Syntax Error at %s" % line
      for x in words[2]:
        assert x in string.digits, "Syntax Error at %s" % line
      curr_funcname = words[1]
      count_logic = 0
      code += [ mark(curr_funcname, assign=True) ]
      code += ['@ SP', 'A=M'] + ['M=0', 'A=A+1'] * int(words[2], 10) + ['D=A', '@ SP', 'M=D']
    elif words[0] == 'call':
      assert len(words)==3, "Syntax Error at %s" % line
      for x in words[2]:
        assert x in string.digits, "Syntax Error at %s" % line
      ret_addr_symbol = '$RET_' + curr_funcname + ':' + str(i)
      code += [ mark(ret_addr_symbol, disable_check=True) ]
      code += ['D=A', '@ SP', 'A=M', 'M=D', '@ SP', 'M=M+1']
      code += ['@ LCL', 'D=M', '@ SP', 'A=M', 'M=D', '@ SP', 'M=M+1']
      code += ['@ ARG', 'D=M', '@ SP', 'A=M', 'M=D', '@ SP', 'M=M+1']
      code += ['@ THIS', 'D=M', '@ SP', 'A=M', 'M=D', '@ SP', 'M=M+1']
      code += ['@ THAT', 'D=M', '@ SP', 'A=M', 'M=D', '@ SP', 'M=M+1']
      code += ['D=M', '@ LCL', 'M=D']
      code += ['@ 5', 'D=D-A', '@ '+words[2], 'D=D-A', '@ ARG', 'M=D']
      code += [ mark(words[1]), '0;JMP']
      code += [ mark(ret_addr_symbol, assign=True, disable_check=True) ]
    elif words[0] == 'return':
      assert len(words)==1, "Syntax Error at %s" % line
      code += ['@ SP', 'D=M', '@ R14', 'M=D']
      code += ['@ ARG', 'D=M', '@ SP', 'M=D+1']
      code += ['@ LCL', 'D=M']
      code += ['@ R15', 'M=D-1', 'A=M', 'D=M', '@ THAT', 'M=D']
      code += ['@ R15', 'M=M-1', 'A=M', 'D=M', '@ THIS', 'M=D']
      code += ['@ R15', 'M=M-1', 'A=M', 'D=M', '@ ARG', 'M=D']
      code += ['@ R15', 'M=M-1', 'A=M', 'D=M', '@ LCL', 'M=D']
      code += ['@ R15', 'M=M-1', 'A=M', 'D=M', '@ R14', 'A=M', 'M=D']
      code += ['A=A-1', 'D=M', '@ SP', 'A=M-1', 'M=D']
      code += ['@ R14', 'A=M', 'A=M', '0;JMP']
    else:
      raise Exception("Syntax Error at %s" % line)
  static_base = static_usage + 1
  return code

def link_check():
  for x,y in symbol_record.items():
    if y==0b01: raise Exception("Function/label %s referenced but undefined" % x)
    if y==0b10: sys.stderr.write("Warning: function/label %s defined but never used\n" % x)

if __name__ == "__main__":
  if len(sys.argv) == 1:
    raise Exception("Require an input file")
  path = './' + sys.argv[1]
  if os.path.isdir(path):
    # An input directory must contain the method "Sys.init" that will be called during startup
    code = get_initial_code()
    for filename in os.listdir(path):
      fpath = path + '/' + filename
      if os.path.isfile(fpath) and fpath[-3:] == '.vm':
        try: fd = open(fpath)
        except: raise Exception("File % not found" % fpath)
        text = fd.read()
        fd.close()
        code += translate(text, filename + '_GLOBAL')
    path = path + '/' + path.split('/')[-1] + '.asm'
  elif os.path.isfile(path) and path[-3:] == ".vm":
    # A single VM input file is a stand-alone code that begins its execution at address 0
    try: fd = open(path)
    except: raise Exception("File % not found" % path)
    text = fd.read()
    fd.close()
    code = translate(text, 'main')
    path = path[:-3] + '.asm'
  else:
    raise Exception("Require a VM file or a directory of VM files")

  link_check()
# print('\n'.join(code))

  f = open(path, 'w')
  f.write('\n'.join(code) + '\n')
  f.close()

