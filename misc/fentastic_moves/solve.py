from stockfish import Stockfish
import sys
import socket
import re

stockfish = Stockfish(path="./stockfish-ubuntu-x86-64-modern", depth=20, parameters={"Threads": 8, "Hash":4096})

piece_mapping = { '♜': 'r', '♞': 'n', '♝': 'b', '♛': 'q', '♚': 'k', '♟': 'p', '♖': 'R', '♘': 'N', '♗': 'B', '♕': 'Q', '♔': 'K', '♙': 'P', ' ': '1' }

def convert(buff):
  buff = buff.split(b'\n')
  acc = []
  for l in buff[1:-2]:
    dec = re.sub(b'\x1b\[[3-4]8;5;[0-9][0-9]?[0-9]?m', b'', re.sub(b'\x1b\[0m', b'', l))[3:-2].decode()[::2]
    for c in dec:
      if c in piece_mapping:
        dec = dec.replace(c, piece_mapping[c])
    for ones in ['1'*c for c in reversed(range(1,10))]:
      dec = dec.replace(ones, str(len(ones)))
    acc.append(dec)
  return f"{'/'.join(acc)} w - - 0 1"


HOST ="94.237.58.211"
PORT = 52600

print(" ========= Starting")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.recv(400)

    for i in range(25):
        buff = s.recv(2000)
        fen = convert(buff)
        stockfish.set_fen_position(fen)
        best_move = stockfish.get_best_move()
        print(f"\x1b[1;33m{i + 1}\x1b[m", fen, '   |   ', best_move)
        s.sendall(f'{best_move}\n'.encode())
        buff = s.recv(400)
        buff.decode().strip('\n')
        buff = s.recv(400)
        print(buff.decode().strip('\n'))
        if buff.startswith(b'Wrong'):
          sys.exit(0)
        if i > 24:
          buff = s.recv(400)
          print(buff.decode().strip('\n'))
          buff = s.recv(400)
          print(buff.decode().strip('\n'))


