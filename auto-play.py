#!/usr/bin/python3

from pwn import *
import sys

host = 'xxx.xxx.xxx.xxx'
port = 5555

conn = remote(host, port)
last_move = ''
last_last_move = ''
previous_last_row = -1

move_left = b'\0xCD'
move_right = b'\0xCB'

while True:
    grid = []
    for i in range(10):
        recv = conn.recvline()
        recv = recv.decode('utf-8', 'ignore').strip()
        print(str(i) + recv)
        grid.append(recv)

    recv = conn.recvline()
    recv = recv.decode('utf-8', 'ignore').strip()
    
    print('m' + recv)

    my_current_pos = recv.find('^')
    my_dead_pos = recv.find('X')
    line_7 = grid[7].find('0')
    line_8 = grid[8].find('0')
    line_9 = grid[9].find('0')

    print("\n\ncurrent pos:" + str(my_current_pos))    
    print('7:' + str(line_7)) 
    print('8:' + str(line_8)) 
    print('9:' + str(line_9))
    print('m:' + str(my_current_pos))

    if my_dead_pos > -1:
        sys.exit()

    if my_current_pos == line_8:
        if my_current_pos + 1 != line_7:
            conn.sendline(move_right)
        elif my_current_pos - 1 != line_7:
            conn.sendline(move_left)
