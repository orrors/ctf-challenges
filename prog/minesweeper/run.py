#!/usr/bin/env python

from websockets.sync.client import connect
import json
from solve import solve
from path import find_path

def printMap(mapp, flags):
    for i, r in enumerate(mapp):
        for j, c in enumerate(r):
            if c == 'covered': print('x',end='')
            elif c == 'key': print('k',end='')
            elif c == 'bomb': print('B',end='')
            elif c == 'c0': print(' ',end='')
            else: print(c.replace('c',''),end='')
        print('  ',end='')
        for j, c in enumerate(r):
            if flags[i][j]:
                print('x', end='')
            else:
                print(' ', end='')

        print()

def play():
    FLAGS = [[False for _ in range(50)] for _ in range(30)]

    with connect("ws://mikusweeper.chals.sekai.team/socket") as websocket:
        while True:
            status = json.loads(websocket.recv())
            # printMap(status['map'])

            if 'flag' in status:
                print(status['flag'])
                return

            # printMap(status['map'], FLAGS)
            x, y, FLAGS = solve(status['map'], FLAGS)

            path = find_path(status, (status['hero']['y'],status['hero']['x']), (x,y))
            print(path, (status['hero']['y'],status['hero']['x']), (x,y))
            print(f"\033[1;33m{status['numKeysRetrieved']}  \033[1;31m{status['livesRemaining']}\033[m")
            # input()
            play = '\n'.join(path)
            websocket.send(play)

play()
