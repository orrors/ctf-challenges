from z3 import BitVec, Solver, sat
password = [BitVec(f'v{i}', 8) for i in range(6)]

s = Solver()
for c in password:
    s.add(97 <= c)
    s.add(c <= 122)
s.add((password[0] & password[2]) == 0x60)
s.add((password[1] | password[4]) == 0x61)
s.add((password[3] ^ password[5]) == 0x6)

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

def all_smt(s, initial_terms):
    def block_term(s, m, t):
        s.add(t != m.eval(t, model_completion=True))
    def fix_term(s, m, t):
        s.add(t == m.eval(t, model_completion=True))
    def all_smt_rec(terms):
        if sat == s.check():
           m = s.model()
           yield m
           for i in range(len(terms)):
               s.push()
               block_term(s, m, terms[i])
               for j in range(i):
                   fix_term(s, m, terms[j])
               yield from all_smt_rec(terms[i:])
               s.pop()
    yield from all_smt_rec(list(initial_terms))

for kk in all_smt(s, password):
    charArrayFromModel(s, password)

