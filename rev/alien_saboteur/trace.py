import gdb

# radare2 breakpoints
# db sym.vm_input sym.vm_store sym.vm_load sym.vm_xor sym.vm_je sym.vm_jne sym.vm_jle sym.vm_jge sym.vm_putc sym.vm_print sym.vm_add sym.vm_addi sym.vm_sub sym.vm_subi sym.vm_mul sym.vm_muli sym.vm_cmp sym.vm_div sym.vm_inv sym.vm_jmp sym.vm_exit sym.vm_push sym.vm_pop sym.vm_mov

gdb.execute('delete breakpoints')
breakpoints = [
		gdb.Breakpoint('vm_input'),
		gdb.Breakpoint('vm_store'),
		gdb.Breakpoint('vm_load'),
		gdb.Breakpoint('vm_xor'),
		gdb.Breakpoint('vm_je'),
		gdb.Breakpoint('vm_jne'),
		gdb.Breakpoint('vm_jle'),
		gdb.Breakpoint('vm_jge'),
		gdb.Breakpoint('vm_putc'),
		gdb.Breakpoint('vm_print'),
		gdb.Breakpoint('vm_add'),
		gdb.Breakpoint('vm_addi'),
		gdb.Breakpoint('vm_sub'),
		gdb.Breakpoint('vm_subi'),
		gdb.Breakpoint('vm_mul'),
		gdb.Breakpoint('vm_muli'),
		gdb.Breakpoint('vm_cmp'),
		gdb.Breakpoint('vm_div'),
		gdb.Breakpoint('vm_inv'),
		gdb.Breakpoint('vm_jmp'),
		gdb.Breakpoint('vm_exit'),
		gdb.Breakpoint('vm_push'),
		gdb.Breakpoint('vm_pop'),
		gdb.Breakpoint('vm_mov')]

gdb.execute('r bin <<< ABCDEFGHIJKL')

count = [0] * len(breakpoints)
save = []
rdi = []
rsi = []


try:
	while True:
		for i,b in enumerate(breakpoints):
			if gdb.selected_frame().name() == b.location:
				count[i]+=1
				save.append(gdb.selected_frame().name())
				if gdb.selected_frame().name() == 'vm_addi':
					rdi.append(gdb.selected_inferior().read_memory( gdb.selected_frame().read_register('rdi').const_value(), 1).tobytes())
					# Pointer to beggining of the string
					rsi.append(gdb.selected_inferior().read_memory( gdb.selected_frame().read_register('rsi').const_value(), 1).tobytes())
		gdb.execute('c')
except Exception as e:
	print(e)
	for b in save:
		print(b.replace('vm_', ''))
	print(rdi)
	print(rsi)
