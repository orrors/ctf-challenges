#!/usr/bin/env -S gdb -q ./suboptimal -nh -x
#
# Run this script or use gdb to call it on gdb
#   -nh prevents loading gdbinit
# gdb -nh ./suboptimal -x find_mapping.py

import gdb

ALPH = '@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|'

flag = list('pctf{AAAAAAAAAAAAAAAAA}')
target = 'xk|nF{quxzwkgzgwx|quitH'

gdb.set_parameter('pagination', False)
b = gdb.Breakpoint('*main+224')
b.silent = True

i_t = 5 # iterate over test characters
while i_t <= 21:
  for att in ALPH:
    flag[i_t] = att
    gdb.execute('r <<< %s' % ''.join(c if c not in ('`','|') else f'\{c}' for c in flag))
    try:
      for index in range(len(flag)):
        rax = chr(gdb.selected_frame().read_register('rax').const_value())
        if index == i_t and rax == target[i_t]:
          print('\033[1;32m    FOUND ', ''.join(flag), '\033[m')
          i_t += 1
          break
        gdb.execute('c')
    except Exception as e:
      pass
gdb.execute('quit')
