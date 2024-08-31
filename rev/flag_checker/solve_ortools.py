from ortools.sat.python import cp_model

model = cp_model.CpModel()
flag = [model.NewIntVar(32, 126, f'f{i}') for i in range(36)]

for i, kc in enumerate('DUCTF{'.encode()):
    model.Add(flag[i] == kc)
model.Add(flag[-1] == ord('}'))

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
        model.Add(sum(selected) == targets[i])
solver = cp_model.CpSolver()
status = solver.Solve(model)
f = [solver.Value(flag[i]) for i in range(36)]
print(bytes(f).decode())
