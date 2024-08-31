from z3 import *

v0 = BitVec('v0',   16)
v1 = BitVec('v1',   16)
v2 = BitVec('v2',   16)
v3 = BitVec('v3',   16)
v4 = BitVec('v4',   16)
v5 = BitVec('v5',   16)
v6 = BitVec('v6',   16)
v7 = BitVec('v7',   16)
v8 = BitVec('v8',   16)
v9 = BitVec('v9',   16)
v10 = BitVec('v10', 16)
v11 = BitVec('v11', 16)
v12 = BitVec('v12', 16)
v13 = BitVec('v13', 16)
v14 = BitVec('v14', 16)
v15 = BitVec('v15', 16)
v16 = BitVec('v16', 16)
v17 = BitVec('v17', 16)
v18 = BitVec('v18', 16)
v19 = BitVec('v19', 16)
v20 = BitVec('v20', 16)
v21 = BitVec('v21', 16)
v22 = BitVec('v22', 16)
v23 = BitVec('v23', 16)
v24 = BitVec('v24', 16)
v25 = BitVec('v25', 16)
v26 = BitVec('v26', 16)
v27 = BitVec('v27', 16)
v28 = BitVec('v28', 16)
v29 = BitVec('v29', 16)
v30 = BitVec('v30', 16)
v31 = BitVec('v31', 16)
v32 = BitVec('v32', 16)
v33 = BitVec('v33', 16)
v34 = BitVec('v34', 16)
v35 = BitVec('v35', 16)
v36 = BitVec('v36', 16)
v37 = BitVec('v37', 16)
v38 = BitVec('v38', 16)
v39 = BitVec('v39', 16)
v40 = BitVec('v40', 16)
# v41 = BitVec('v41', 8)
res = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,
       v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40]

# ((((((*(param_1 + 9) + -0x7a) - (int)*(param_1 + 0x1b) == -0xb8) &&
#       (*(param_1 + 0x10) == '1')) &&
#      ((*(param_1 + 0x10) + 0x3c) - (int)*(param_1 + 0x25) == -8)) &&
#     (((int)*(param_1 + 0xd) + *(param_1 + 0x1d) + 0x32 == 0x109 &&
#      (*(param_1 + 0x15) * 2 + (int)*(param_1 + 0x1d) == 0x13c)))) &&
#    ((*(param_1 + 9) == '7' &&
#     (((int)*(param_1 + 0x25) == *(param_1 + 0x1d) + 5 &&
#      (*(param_1 + 0x10) * 2 + (int)*(param_1 + 0x1d) == 0xd2))))))

s = Solver()

for K in res:
  s.add(32 <= K, K <= 126)

s.add(v0 == 0x48, v1 == 0x54, v2 == 0x42, v3 == 0x7b, v40 == 0x7d) # HTB{

s.add(v9 - 0x7a - v27 == -0xb8)
s.add(v16 == ord('1'))
s.add(v16 + 0x3c - v37 == -8)
s.add(v13 + v29 + 0x32 == 0x109)
s.add(v21 * 2 + v29 == 0x13c)
s.add(v9 == ord('7'))
s.add(v37 == v29 + 5)
s.add(v16 * 2 + v29 == 0xd2)

# if (((((*(param_1 + 0x14) == '_') &&
#       ((int)*(param_1 + 0x20) + *(param_1 + 0xb) + -0x14 == 0x84)) &&
#      ((int)*(param_1 + 8) == *(param_1 + 0x18) * -10 + 0x475)) &&
#     (((int)*(param_1 + 0x23) + *(param_1 + 0x12) + -0x32 == 0xba &&
#      ((int)*(param_1 + 0x17) + (int)*(param_1 + 4) == 0x61)))) &&
#    (((int)*(param_1 + 0x1a) + *(param_1 + 10) + -0x22 == 0x7f &&
#     ((*(param_1 + 0x22) + 0x32 == (*(param_1 + 0xf) + -0x31) * 2 &&
#      ((int)*(param_1 + 0x13) + *(param_1 + 0x26) + 0xfd == 0x1e4)))))) {

s.add(v20 == ord('_'))
s.add(v32 + v11 - 0x14 == 0x84)
s.add(v8 == v24 * -10 + 0x475)
s.add(v35 + v18 - 0x32 == 0xba)
s.add(v23 + v4 == 0x61)
s.add(v26 + v10 - 0x22 == 0x7f)
s.add(v34 + 0x32 == (v15 - 0x31) * 2)
s.add(v19 + v38 + 0xfd == 0x1e4)

# if ((((*(param_1 + 0x24) * 5 + -0x32 == *(param_1 + 0x11) + 0x44) &&
#      ((int)*(param_1 + 0x16) + *(param_1 + 0x27) + -0x28 == 0xae)) &&
#     (*(param_1 + 0x16) * 5 + *(param_1 + 0x19) + -10 == 0x28f)) &&
#    (((*(param_1 + 7) * 5 == *(param_1 + 0x1e) + 0x1d2 &&
#      ((int)*(param_1 + 0x1f) + *(param_1 + 0xc) + 0x45 == 0x121)) &&
#     (((int)*(param_1 + 0x24) + *(param_1 + 0xe) + 0x79 == 0x108 &&
#      (*(param_1 + 0x27) * 3 + (int)*(param_1 + 0x11) == 0x1a6)))))) {

s.add(v36 * 5 - 0x32 == v17 + 0x44)
s.add(v22 + v39 - 0x28 == 0xae)
s.add(v22 * 5 + v25 - 10 == 0x28f)
s.add(v7 * 5 == v30 + 0x1d2)
s.add(v31 + v12 + 0x45 == 0x121)
s.add(v36 + v14 + 0x79 == 0x108)
s.add(v39 * 3 + v17 == 0x1a6)

## weird code section @ 0x00401601

s.add(v37 + 0x1ef == v21 * 6)
s.add(v16 + v33 == 0x90)
s.add(v20 * 4 + v11 == 0x1ad)
s.add(v32 - 0x34 == v8)
s.add(v18 * 8 - v18 + v24  == 0x3c3)
s.add(v35 + (v6 * 4 + v6) * 2 == 0x428)
s.add(v28 + 0xd == v18)

## weird code section @ 0x004018cb

s.add(v23 == 0x30)
s.add(v4 + 0x32  == v26 - 7)
s.add(v10 + 0x53 + v34 * 2 == 0xf2)
s.add(v15 * 4 + v15 + 0x14 + v38 == 0x276)
s.add(v39 - 0x28 + v5 == 0xa9)
s.add(v25 + v7 == 0xc6)
s.add(v30 + v12 * 4 + v12 == 0x257)

s.check()
m = s.model()

xx = sorted((c for c in s.model()), key=lambda x: [ str(k) for k in res].index(str(x)))
k = {str(x): s.model()[x].as_long() for x in xx}
result = ''.join((chr(k['v'+str(i)]) if k['v'+str(i)] <= 126 else '░') if 'v'+str(i) in k else '░' for i in range(41))
print(result)
