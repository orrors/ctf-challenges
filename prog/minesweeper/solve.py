from solver import Solver
from solver.policies import corner_then_edge2_policy, random_policy
import numpy as np
import random

def setFlag(flags, x, y):
    flags[x][y] = True

def mapConvert(mapp, flags):
    newMap = np.zeros((len(mapp), len(mapp[0])), dtype=np.float64)
    for i in range(newMap.shape[0]):
        for j in range(newMap.shape[1]):
            c=mapp[i][j]
            if c == 'covered':
                newMap[i][j]=np.nan
                # if flags[i][j]: newMap[i][j]='flag'
                # else: newMap[i][j]=np.nan
            elif c.startswith('c'):
                newMap[i][j]=int(c[1:])
    return newMap

def findKey(mapp):
    for i, r in enumerate(mapp):
        for j, c in enumerate(r):
            if c == 'key':
                return i, j
    return -1, -1

def printMap(mapp):
    for r in mapp:
        for c in r:
            if type(c) != str and np.isnan(c): print('x', end='')
            elif c == 'flag': print('F', end='')
            elif c == 'key': print('K', end='')
            elif c == 0: print(' ', end='')
            else: print(c, end='')
        print()

def solve(mapp, flags):
    h=len(mapp)
    w=len(mapp[0])
    x, y=findKey(mapp)
    if x != -1 and y != -1:
        return x, y, flags

    solver=Solver(w, h, 150)
    state=mapConvert(mapp, flags)
    prob=solver.solve(state)
    # Flag newly found mines.
    for y, x in zip(*((prob == 1) & (state != "flag")).nonzero()):
        setFlag(flags, y, x)
    best_prob=np.nanmin(prob)
    ys, xs=(prob == best_prob).nonzero()
    # ys,xs=(prob < 1).nonzero()
    k = list(zip(xs,ys))
    print(len(k),(~np.isnan(prob)).nonzero())
    random.shuffle(k)
    for x, y in k:
        return y, x, flags
