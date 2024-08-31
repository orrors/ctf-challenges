from z3 import BitVec, Solver
flag = [BitVec(f'v{i}', 8) for i in range(32)]

s = Solver()
# limit to printable range
for c in flag:
    s.add(0x20 <= c)
    s.add(c <= 0x7e)

# ((((((((pcVar1[0x1d] == ((pcVar1[5] - pcVar1[3]) + 'F')) &&
s.add(flag[0x1d] == (flag[5] - flag[3] + ord('F')))
# ((pcVar1[2] + pcVar1[0x16]) == (pcVar1[0xd] + '{'))) &&
s.add((flag[2] + flag[0x16]) == (flag[0xd] + ord('{')))
# ((pcVar1[0xc] + pcVar1[4]) == (pcVar1[5] + '\x1c'))) &&
s.add((flag[0xc] + flag[4]) == (flag[5] + 0x1c))
# ((pcVar1[0x19] * pcVar1[0x17]) == (*pcVar1 + pcVar1[0x11] + '\x17')
s.add((flag[0x19] * flag[0x17]) == (flag[0] + flag[0x11] + 0x17))
# ((pcVar1[0x1b] * pcVar1[1]) == (pcVar1[5] + pcVar1[0x16] + -0x15))
s.add((flag[0x1b] * flag[1]) == (flag[5] + flag[0x16] + -0x15))
# ((pcVar1[9] * pcVar1[0xd]) == (pcVar1[0x1c] * pcVar1[3] + -9)
s.add((flag[9] * flag[0xd]) == (flag[0x1c] * flag[3] + -9))
# (pcVar1[9] == 'p'
s.add(flag[9] == ord('p'))
# ((pcVar1[0x13] + pcVar1[0x15]) == (pcVar1[6] + -0x80)
s.add((flag[0x13] + flag[0x15]) == (flag[6] + -0x80))
# (pcVar1[0x10] == ((pcVar1[0xf] - pcVar1[0xb]) + '0')
s.add(flag[0x10] == (flag[0xf] - flag[0xb] + ord('0')))
# ((pcVar1[7] * pcVar1[0x1b]) == (pcVar1[1] * pcVar1[0xd] + '-')
s.add((flag[7] * flag[0x1b]) == (flag[1] * flag[0xd] + ord('-')))
# (pcVar1[0xd] == (pcVar1[0x12] + pcVar1[0xd] + -0x65)
s.add(flag[0xd] == (flag[0x12] + flag[0xd] + -0x65))
# ((pcVar1[0x14] - pcVar1[8]) == (pcVar1[9] + '|')
s.add((flag[0x14] - flag[8]) == flag[9] + ord('|'))
# (pcVar1[0x1f] == ((pcVar1[8] - pcVar1[0x1f]) + -0x79)
s.add(flag[0x1f] == ((flag[8] - flag[0x1f]) + -0x79))
# ((pcVar1[0x14] * pcVar1[0x1f]) == (pcVar1[0x14] + '\x04')
s.add((flag[0x14] * flag[0x1f]) == (flag[0x14] + 0x04))
# ((pcVar1[0x18] - pcVar1[0x11]) == (pcVar1[0x15] + pcVar1[8] + -0x17)
s.add((flag[0x18] - flag[0x11]) == (flag[0x15] + flag[8] + -0x17))
# ((pcVar1[7] + pcVar1[5]) == (pcVar1[5] + pcVar1[0x1d] + ',')
s.add((flag[7] + flag[5]) == (flag[5] + flag[0x1d] + ord(',')))
# ((pcVar1[0xc] * pcVar1[10]) == ((pcVar1[1] - pcVar1[0xb]) + -0x24)
s.add((flag[0xc] * flag[10]) == ((flag[1] - flag[0xb]) + -0x24))
# ((pcVar1[0x1f] * *pcVar1) == (pcVar1[0x1a] + -0x1b)
s.add((flag[0x1f] * flag[0]) == (flag[0x1a] + -0x1b))
# ((pcVar1[1] + pcVar1[0x14]) == (pcVar1[10] + -0x7d)
s.add((flag[1] + flag[0x14]) == (flag[10] + -0x7d))
# (pcVar1[0x12] == (pcVar1[0x1b] + pcVar1[0xe] + '\x02')
s.add(flag[0x12] == (flag[0x1b] + flag[0xe] + 0x02))
# ((pcVar1[0x1e] * pcVar1[0xb]) == (pcVar1[0x15] + 'D')
s.add((flag[0x1e] * flag[0xb]) == (flag[0x15] + ord('D')))
# ((pcVar1[5] * pcVar1[0x13]) == (pcVar1[1] + -0x2c)
s.add((flag[5] * flag[0x13]) == (flag[1] + -0x2c))
# ((pcVar1[0xd] - pcVar1[0x1a]) == (pcVar1[0x15] + -0x7f)
s.add((flag[0xd] - flag[0x1a]) == (flag[0x15] + -0x7f))
# (pcVar1[0x17] == ((pcVar1[0x1d] - *pcVar1) + 'X')
s.add(flag[0x17] == ((flag[0x1d] - flag[0]) + ord('X')))
# (pcVar1[0x13] == (pcVar1[8] * pcVar1[0xd] + -0x17)
s.add(flag[0x13] == (flag[8] * flag[0xd] + -0x17))
# ((pcVar1[6] + pcVar1[0x16]) == (pcVar1[3] + 'S')
s.add((flag[6] + flag[0x16]) == (flag[3] + ord('S')))
# (pcVar1[0xc] == (pcVar1[0x1a] + pcVar1[7] + -0x72)
s.add(flag[0xc] == (flag[0x1a] + flag[7] + -0x72))
# (pcVar1[0x10] == ((pcVar1[0x12] - pcVar1[5]) + '3')
s.add(flag[0x10] == ((flag[0x12] - flag[5]) + ord('3')))
# ((pcVar1[0x1e] - pcVar1[8]) == (pcVar1[0x1d] + -0x4d)
s.add((flag[0x1e] - flag[8]) == (flag[0x1d] + -0x4d))
# ((pcVar1[0x14] - pcVar1[0xb]) == (pcVar1[3] + -0x4c)
s.add((flag[0x14] - flag[0xb]) == (flag[3] + -0x4c))
# ((pcVar1[0x10] - pcVar1[7]) == (pcVar1[0x11] + 'f')
s.add((flag[0x10] - flag[7]) == (flag[0x11] + ord('f')))
# ((pcVar1[1] + pcVar1[0x15]) == (pcVar1[0xb] + pcVar1[0x12] + '+'
s.add((flag[1] + flag[0x15]) == (flag[0xb] + flag[0x12] + ord('+')))

s.check()

def charArrayFromModel(model, array, varFormat=lambda i: f'v{str(i)}'):
    '''Converts a model results into a printable ascii values
    Params:
        model - a checked z3.Solver
        array - array of numbered variables
        varFormat - optional function that given an array index returns the variable's name
    '''
    xx = sorted((c for c in model.model()), key=lambda x: [
        str(k) for k in array].index(str(x)))
    k = {str(x): model.model()[x].as_long() for x in xx}
    result = ''.join((chr(k[varFormat(i)]) if 0x20 <= k[varFormat(i)] <=
                      0x7e else '░') if varFormat(i) in k else '░' for i in range(len(array)))
    print(result)

charArrayFromModel(s, flag)
