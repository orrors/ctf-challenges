
# create the dictionary
d = {k:(123*k+18)%256 for k in range(32,128)}

buff = bytes.fromhex(open('msg.enc', 'r').read())
for c in buff:
  for k in d:
    if d[k] == c:
      print(chr(k), end='')
