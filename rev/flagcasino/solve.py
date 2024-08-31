from ctypes import CDLL
libc = CDLL('libc.so.6')

ALPHABET = [k for k in range(20,126)]

f = open('seed', 'rb')
def read():
	while True:
		d = int.from_bytes(f.read(4), 'little')
		if d: yield d
		else: break

for data in read():
	for letter in ALPHABET:
		libc.srand(letter)
		k = libc.rand()
		if k == data:
			print(chr(letter), end='')
print()

