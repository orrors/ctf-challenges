import socket
import re

HOST ="206.189.24.162"
PORT = 30174
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	while True:
		buff = s.recv(2**12)
		match = re.findall(r'\[\d\d\d\]: (.*) = ?', buff.decode())
		if len(match) == 0: print(buff); break
		e = match[0]
		while re.search('\+', e):
			e = re.sub(r'\([0-9]+\)', lambda x: str(eval(x[0])), e)
			e = re.sub(r'\([0-9]+ [*+] [0-9]+\)', lambda x: str(eval(x[0])), e)
			e = re.sub(r'(([0-9]+ \+ )+[0-9]+)', lambda x: str(eval(x[0])), e)
			e = re.sub(r'\((([0-9]+ \* )+[0-9]+)\)', lambda x: str(eval(x[0])), e)
		r = eval(e)
		print(r)
		s.sendall(f'{r}\n'.encode())

