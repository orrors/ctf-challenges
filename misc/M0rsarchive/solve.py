from PIL import Image
import os

MORSE_DICT = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')'}

def decode_image(path):
	im = Image.open(path, 'r')
	width, height = im.size
	px = list(im.getdata())
	counts = list((c, px.count(c)) for c in set(px))
	EMPTY = max(counts, key=lambda x: x[1])[0] # should be the color with the most ammount of pixels
	pwd = ''
	for i in range(0, width*height, width):
			line = ''.join(' ' if f == EMPTY else 'x' for f in px[i:i+width]) # put x where there's a different color
			if 'x' in line:
				pwd += MORSE_DICT[''.join('-' if len(c) == 3 else '.' for c in line.split())] # convert to morse code letter
	return pwd

def extract(path, pwd_img):
	pwd = decode_image(pwd_img)
	os.system(f'unzip -P {pwd} {path}')

for i in range(999, -1, -1):
	extract(f'flag_{i}.zip', 'pwd.png')
	os.system('mv flag/* .')
	os.system('rmdir flag')
