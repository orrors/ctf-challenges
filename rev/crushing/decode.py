FLAG = [' '] * 1000
with open('message.txt.cz', 'rb') as fp:
	for bt in range(0x00, 0x7e):
		size = fp.read(8)
		size_i = int.from_bytes(size, 'little')
		if size_i > 0:
			for k in range(size_i):
				b = fp.read(8)
				FLAG[int.from_bytes(b, 'little')] = chr(bt)
print(''.join(FLAG))

