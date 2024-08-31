import gdb
import time

ALPH = '@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz{}0123456789'
flag = list('DUCTF{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}')
b = gdb.Breakpoint('*0x000055555555d0f3')

def get_memory_register(reg):
	register_value = gdb.parse_and_eval(f"${reg}")
	address = int(register_value)
	inferior = gdb.selected_inferior()
	memory_contents = inferior.read_memory(address, 44)
	return memory_contents.tobytes()

def compare(hexa, hexb, it):
	a,b =hexa[:(it+1)*2],hexb[:(it+1)*2]
	print(a,b,a==b)
	if a==b:return True
	return False

i_t = 6
while i_t <= 43:
	for att in ALPH:
		flag[i_t] = att
		gdb.execute('r <<< %s' % ''.join(c if c not in ('`','|') else f'\{c}' for c in flag))
		print('r <<< %s' % ''.join(c if c not in ('`','|') else f'\{c}' for c in flag))
		rsi = get_memory_register('rsi')
		rdi = get_memory_register('rdi')
		if compare(rsi.hex(), rdi.hex(), i_t):
			print('\033[1;32m    FOUND ', ''.join(flag), '\033[m')
			time.sleep(2)
			i_t += 1
			break
