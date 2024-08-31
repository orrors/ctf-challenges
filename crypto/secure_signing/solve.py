from hashlib import sha256
import socket
import re

HOST="206.189.28.151"
PORT=30708

def verify(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.recv(1024)
    s.sendall(b'1\n')
    s.recv(1024)
    s.sendall(msg + b'\n')
    r = s.recv(1024).decode()
    h = re.search(r'Hash: (\w+)', r)
    s.close()
    return h.group(1)

def xor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])

def H(m):
    return sha256(m).digest()

# this should be set to an empty string. some
flag = b""

for _ in range(40):
    test_string = b"a"*(len(flag)+1)
    try:
        target_hash = verify(test_string)
    except AttributeError:
        target_hash = verify(test_string)

    for i in range(ord(' '), ord('~')):
        test_hash = H(xor(test_string, flag + chr(i).encode())).hex()
        if test_hash == target_hash:
            flag += chr(i).encode()
            print(flag)
            break

