from z3 import *

v80 = BitVec('v80', 8); v7f = BitVec('v7f', 8); v7e = BitVec('v7e', 8); v7d = BitVec('v7d', 8); v7c = BitVec('v7c', 8); v7b = BitVec('v7b', 8); v7a = BitVec('v7a', 8); v79 = BitVec('v79', 8); v78 = BitVec('v78', 8); v77 = BitVec('v77', 8); v76 = BitVec('v76', 8); v75 = BitVec('v75', 8); v74 = BitVec('v74', 8); v73 = BitVec('v73', 8); v72 = BitVec('v72', 8); v71 = BitVec('v71', 8); v70 = BitVec('v70', 8); v6f = BitVec('v6f', 8); v6e = BitVec('v6e', 8); v6d = BitVec('v6d', 8); v6c = BitVec('v6c', 8); v6b = BitVec('v6b', 8); v6a = BitVec('v6a', 8); v69 = BitVec('v69', 8); v68 = BitVec('v68', 8); v67 = BitVec('v67', 8); v66 = BitVec('v66', 8); v65 = BitVec('v65', 8); v64 = BitVec('v64', 8); v63 = BitVec('v63', 8); v62 = BitVec('v62', 8); v61 = BitVec('v61', 8); v60 = BitVec('v60', 8); v5f = BitVec('v5f', 8); v5e = BitVec('v5e', 8); v5d = BitVec('v5d', 8); v5c = BitVec('v5c', 8); v5b = BitVec('v5b', 8); v5a = BitVec('v5a', 8); v59 = BitVec('v59', 8); v58 = BitVec('v58', 8); v57 = BitVec('v57', 8); v56 = BitVec('v56', 8); v55 = BitVec('v55', 8); v54 = BitVec('v54', 8); v53 = BitVec('v53', 8); v52 = BitVec('v52', 8); v51 = BitVec('v51', 8); v50 = BitVec('v50', 8); v4f = BitVec('v4f', 8); v4e = BitVec('v4e', 8); v4d = BitVec('v4d', 8); v4c = BitVec('v4c', 8); v4b = BitVec('v4b', 8); v4a = BitVec('v4a', 8); v49 = BitVec('v49', 8); v48 = BitVec('v48', 8); v47 = BitVec('v47', 8); v46 = BitVec('v46', 8); v45 = BitVec('v45', 8); v44 = BitVec('v44', 8);

res = [ v80, v7f, v7e, v7d, v7c, v7b, v7a, v79, v78, v77, v76, v75, v74, v73, v72, v71, v70, v6f, v6e, v6d, v6c, v6b, v6a, v69, v68, v67, v66, v65, v64, v63, v62, v61, v60, v5f, v5e, v5d, v5c, v5b, v5a, v59, v58, v57, v56, v55, v54, v53, v52, v51, v50, v4f, v4e, v4d, v4c, v4b, v4a, v49, v48, v47, v46, v45, v44]

s = Solver()
s.add(v80 == 0x48, v7f == 0x54, v7e == 0x42, v7d == 0x7b) # HTB{
s.add(v6b * v50 == 0x14,)
s.add(v60 - v5c == 0xfa,)
s.add(v5b - v66 == 0xd6,)
s.add(v70 - v50 == 0x8,)
s.add(v49 - v78 == 0xd5,)
s.add(v66 * v79 == 0xed,)
s.add(v7c * v68 == 0xc8,)
s.add(v64 ^ v5e == 0x55,)
s.add(v62 - v49 == 0x34,)
s.add(v4e + v45 == 0x8f,)
s.add(v65 + v54 == 0xd6,)
s.add(v72 ^ v6f == 0x31,)
s.add(v48 * v6c == 0xac,)
s.add(v46 - v66 == 0xc2,)
s.add(v7a ^ v66 == 0x2f,)
s.add(v59 ^ v72 == 0x5a,)
s.add(v59 ^ v54 == 0x40,)
s.add(v4f + v69 == 0x98,)
s.add(v69 * v45 == 0x68,)
s.add(v7f - v64 == 0xdb,)
s.add(v68 - v63 == 0xd2,)
s.add(v5a - v68 == 0x2e,)
s.add(v6a ^ v60 == 0x1a,)
s.add(v54 * v7c == 0xa0,)
s.add(v5a * v65 == 0x5e,)
s.add(v71 - v58 == 0xc8,)
s.add(v4b ^ v4f == 0x56,)
s.add(v53 ^ v66 == 0x2b,)
s.add(v77 ^ v4a == 0x19,)
s.add(v64 - v51 == 0x1a,)
s.add(v6d + v4e == 0xa1,)
s.add(v47 + v5b == 0x56,)
s.add(v6e ^ v63 == 0x38,)
s.add(v44 ^ v54 == 0x9,)
s.add(v71 * v5a == 0x79,)
s.add(v62 ^ v5b == 0x5d,)
s.add(v7e * v60 == 0x5c,)
s.add(v76 * v6e == 0x39,)
s.add(v5d * v6b == 0x2f,)
s.add(v78 * v5b == 0xab,)
s.add(v66 + v59 == 0x93,)
s.add(v5e ^ v66 == 0x73,)
s.add(v61 ^ v6c == 0x40,)
s.add(v70 + v67 == 0xa9,)
s.add(v45 ^ v59 == 0x15,)
s.add(v45 + v80 == 0x69,)
s.add(v52 + v5e == 0xa5,)
s.add(v4c ^ v62 == 0x37,)
s.add(v80 * v64 == 0x8,)
s.add(v5e - v48 == 0xc5,)
s.add(v44 + v6e == 0xe4,)
s.add(v58 ^ v5d == 0x6e,)
s.add(v48 * v70 == 0xac,)
s.add(v4a - v51 == 0xd,)
s.add(v49 + v62 == 0x9c,)
s.add(v5f + v7a == 0xd4,)
s.add(v79 * v63 == 0xed,)
s.add(v63 ^ v48 == 0x38,)
s.add(v7f * v5b == 0x64,)
s.add(v46 ^ v48 == 0x46,)
s.add(v7e * v6d == 0x26,)
s.add(v6a ^ v66 == 0x2b,)
s.add(v79 + v7f == 0x87,)
s.add(v80 ^ v65 == 0x2a,)
s.add(v6b - v7f == 0xb,)
s.add(v4a + v65 == 0xce,)
s.add(v73 ^ v6f == 0x3b,)
s.add(v6d - v46 == 0x12,)
s.add(v72 - v46 == 0x4d,)
s.add(v56 * v4c == 0x4e,)
s.add(v4d ^ v51 == 0x38,)
s.add(v67 + v5a == 0x94,)
s.add(v4c + v57 == 0xcf,)
s.add(v67 + v74 == 0x66,)
s.add(v5c + v44 == 0xf1,)
s.add(v57 - v6b == 0x11,)
s.add(v5c - v4f == 0x44,)
s.add(v77 - v5d == 0x44,)
s.add(v4d ^ v4b == 0x1,)
s.add(v47 ^ v5e == 0xd,)
s.add(v75 - v64 == 0xeb,)
s.add(v68 + v69 == 0x99,)
s.add(v73 + v68 == 0x95,)
s.add(v74 - v80 == 0xe9,)
s.add(v61 + v5e == 0x60,)
s.add(v4b + v7b == 0x96,)
s.add(v4f * v56 == 0x60,)
s.add(v50 * v6b == 0x14,)
s.add(v65 - v4c == 0x3,)
s.add(v6c + v47 == 0x95,)
s.add(v76 * v4b == 0xda,)
s.add(v57 + v7f == 0xc4,)
s.add(v51 - v7f == 0xb,)
s.add(v51 + v59 == 0x93,)
s.add(v74 * v46 == 0x51,)
s.add(v78 * v66 == 0x41,)
s.add(v52 - v61 == 0x45,)
s.add(v5b + v79 == 0x68,)
s.add(v7c + v5c == 0xbc,)
s.add(v60 + v61 == 0xa2,)
s.add(v7b + v67 == 0x65,)
s.add(v55 * v63 == 0xed,)
s.add(v53 ^ v73 == 0x10,)
s.add(v50 - v74 == 0x3b,)
s.add(v69 - v78 == 0x9,)
s.add(v56 ^ v79 == 0x41,)
s.add(v7b - v55 == 0xfd,)
s.add(v6e ^ v44 == 0x1a,)
s.add(v7d ^ v7f == 0x2f,)
s.add(v6f - v59 == 0x2b,)
s.add(v6c + v78 == 0xd3,)
s.add(v75 * v4b == 0xd8,)
s.add(v7a + v65 == 0xd2,)
s.add(v7d + v7b == 0xab,)
s.add(v5d - v51 == 0xd2,)
s.add(v5f ^ v70 == 0x10,)

# movzx  edx,BYTE PTR [rbp-0x58]
# movzx  eax,BYTE PTR [rbp-0x66]
# cmp    dl,al
# jne    0x555555555ac1 <main+2396>
# movzx  edx,BYTE PTR [rbp-0x63]
# movzx  eax,BYTE PTR [rbp-0x6b]
# cmp    dl,al
# jne    0x555555555ac1 <main+2396>
# movzx  edx,BYTE PTR [rbp-0x6f]
# movzx  eax,BYTE PTR [rbp-0x76]
# cmp    dl,al
# jne    0x555555555ac1 <main+2396>
# movzx  edx,BYTE PTR [rbp-0x4e]
# movzx  eax,BYTE PTR [rbp-0x60]
# cmp    dl,al
# jne    0x555555555ac1 <main+2396>
# movzx  edx,BYTE PTR [rbp-0x54]
# movzx  eax,BYTE PTR [rbp-0x6c]
# cmp    dl,al
# jne    0x555555555ac1 <main+2396>
# movzx  edx,BYTE PTR [rbp-0x55]
# movzx  eax,BYTE PTR [rbp-0x6d]
# cmp    dl,al
# jne    0x555555555ac1 <main+2396>

s.check()
# s.model()

xx = sorted((c for c in s.model()), key=lambda x: [str(k) for k in res].index(str(x)))
print([str(x) for x in xx])
print(''.join([chr(x) for x in (s.model()[c].as_long() for c in xx)]))


