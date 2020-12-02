import sys
import string

symbol_table = {
  'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 
  'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,  
  'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'SCREEN': 0x4000, 'KBD': 0x6000
}
symbol_next_address = 0x10

def serial(word, assign):
  global symbol_table, symbol_next_address
  if assign != None:
    if word in symbol_table:
      raise Exception('Repeated declaration of label %s' % word)
    symbol_table[word] = assign
    return 0
  if word not in symbol_table:
    symbol_table[word] = symbol_next_address
    symbol_next_address += 1
  return symbol_table[word]

def translate(label, word): # label = 'a', 'j', 'w', 'c', or number
  ascii_symbol = string.ascii_letters + string.digits + "_.$:"
  if label == 'a': # word != ''
    if word[0] in string.digits:
      for x in word:
        if x not in string.digits:
          raise Exception('Syntax Error at "%s"' % word)
      address = int(word, 10)
      if address >= 2**15:
        raise Exception('%s too large' % word)
      return address
    else:
      for x in word:
        if x not in ascii_symbol:
          raise Exception('Syntax Error at "%s"' % word)
      return serial(word, None)

  if label == 'j':
    J_asm = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
    for i, j in enumerate(J_asm):
      if word == j:
        return i * (2**0)
    raise Exception('Syntax Error at "%s"' % word)

  if label == 'w':
    W_asm = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'ADM']
    for i, w in enumerate(W_asm):
      if word == w:
        return i * (2**3)
    raise Exception('Syntax Error at "%s"' % word)

  if label == 'c':
    C_asm = {
        '1': 0b0111111,         '0': 0b0101010, 
       '-1': 0b0111010,         'D': 0b0001100, 
        'A': 0b0110000,         'M': 0b1110000, 
       '!D': 0b0001101,        '!A': 0b0110001,    
       '!M': 0b1110001,        '-D': 0b0001111, 
       '-A': 0b0110011,        '-M': 0b1110011, 
      'D+1': 0b0011111,       'A+1': 0b0110111,    
      'M+1': 0b1110111,       'D-1': 0b0001110, 
      'A-1': 0b0110010,       'M-1': 0b1110010, 
      'D+A': 0b0000010,       'D+M': 0b1000010, 
      'D-A': 0b0010011,       'D-M': 0b1010011, 
      'A-D': 0b0000111,       'M-D': 0b1000111, 
      'D&A': 0b0000000,       'D&M': 0b1000000, 
      'D|A': 0b0010101,       'D|M': 0b1010101, 
    }
    for c, r in C_asm.items():
      if word == c:
        return r * (2**6)
    raise Exception('Syntax Error at "%s"' % word)

  # label is a number
  for x in word: # word != ''
    if x not in ascii_symbol:
      raise Exception('Syntax Error at "%s"' % word)
  return serial(word, label)
  
def parser(text):
  code = []
  lines = list(map(lambda x: x.split('//')[0].strip(), text.split('\n')))
  lines = list(filter(None, lines))

  skipped = 0
  for idx, line in enumerate(lines):
    type_l = line.split('(')
    if len(type_l) == 1: continue
    if len(type_l)>2 or type_l[0].strip() != '':
      raise Exception('Syntax Error at "%s"' % line)
    type_l = type_l[1].split(')')
    if len(type_l) != 2 or type_l[1].strip() != '' or type_l[0].strip() == '':
      raise Exception('Syntax Error at "%s"' % line)
    translate(idx-skipped, type_l[0].strip())
    skipped += 1

  for line in lines:
    if '(' in line: continue

    type_a = line.split('@')
    if len(type_a)>1:
      if len(type_a)>2 or type_a[0].strip() != ''or type_a[1].strip() == '':
        raise Exception('Syntax Error at "%s"' % line)
      code.append( translate('a', type_a[1].strip()) )
      continue

    type_j = line.split(';')
    j_code = 0
    if len(type_j)>1:
      if len(type_j)>2: 
        raise Exception('Syntax Error at "%s"' % line)
      j_code = translate('j', type_j[1].strip())
      line = type_j[0].strip()

    type_w = line.split('=')
    w_code = 0
    if len(type_w)>1:
      if len(type_w)>2: 
        raise Exception('Syntax Error at "%s"' % line)
      w_code = translate('w', type_w[0].strip())
      line = type_w[1].strip()

    c_code = translate('c', line)
    code.append( (0b111*(2**13)) | c_code | w_code | j_code )

  return code


if __name__ == "__main__":
  if len(sys.argv)==1:
    raise Exception("Require an input file")
  filename = sys.argv[1]
  if len(filename) <= 4 or filename[-4:] != ".asm":
    raise Exception("Require an assembly file")
  try:
    fd = open(filename)
  except:
    raise Exception("File %s not found" % filename)
  text = fd.read()
  fd.close()
  code = parser(text)
  binary = list(map(lambda x: '{:016b}'.format(x), code))
  print('\n'.join(binary))

