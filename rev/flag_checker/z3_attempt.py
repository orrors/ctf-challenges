from z3 import BitVec, Sum, Solver

INPUT_LEN = 36
flag = [BitVec(f'v{i}', 8) for i in range(INPUT_LEN)]

s = Solver()
for i,c in enumerate('DUCTF{'.encode()):
    s.add(flag[i] == c)
s.add(flag[-1] == ord('}'))

with open('ms_flag_checker', 'rb') as binF:
    N_CHECKS = 26
    binF.seek(0x3060) # seek targets
    # read 4 bytes each time but use only the first 2 because the padding is like this:
    #  00003060: a105 0000 fb07 0000 eb04 0000 ef07 0000  ................
    targets = [int.from_bytes(binF.read(4)[:2], 'little') for _ in range(N_CHECKS)]

    binF.seek(0x30e0) # seek mask
    for i in range(N_CHECKS):
        buff = binF.read(0x18).strip(b'\0') # removing trailings 0s
        k = [[1]*c if c <= 0x7f else [0]*(0x100 - c) for c in buff]
        k = [i for r in k for i in r]  # flatten
        selected = [flag[i] for i, c in enumerate(k) if c == 1]
        # print(targets[i], selected)
        print(Sum(selected))
        s.add(Sum(selected) == targets[i])

s.check()
# print(s.model())

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
