#!/usr/bin/python3

# WARNING: This is terrible code that certainly does not follow best practices.
# It was written in a rush to capture the flag at the last minute. I've uploaded
# it as is so you can learn from my mistages :)

from pwn import *
import sys

host = 'challs.xmas.htsp.ro'
port = 6051

conn = remote(host, port)

def next_question():
    answer = ''
    for i in range(5):
        recv = conn.recvline()
        recv = recv.decode('utf-8', 'ignore').strip()
        print(recv)
        
        # Get array and sort
        if(i == 2):
            print(recv)
            array = recv[9:-1].replace(" ", "").split(',')
            for i in range(0, len(array)): 
                array[i] = int(array[i]) 

            sorted_l2h = sorted(array)
            sorted_h2l = sorted(array, reverse=True)       
        
        # Get first key
        if(i == 3):
            key1 = recv[5:]
            
        # Get second key
        if(i == 4):
            key2 = recv[5:]
                
    # Build answer
    answer = ''
    print(array)
    print(sorted_l2h)
    print(sorted_h2l)
    print(key1)
    print(key2)

    for i in range( int(key1) ):
        answer = answer + str(sorted_l2h[i]) + ', '

    answer = answer[:-2]
    answer = answer + "; "

    for i in range( int(key2) ):
        answer = answer + str(sorted_h2l[i]) + ', '

    answer = answer[:-2]

    print(answer)

    conn.sendline( answer )
    next_question()
    
    # Get first key
    if(i == 3):
        key1 = recv[5:]
        
    # Get second key
    if(i == 4):
        key2 = recv[5:]
            
    # Build answer
    answer = ''
    print(array)
    print(sorted_l2h)
    print(sorted_h2l)
    print(key1)
    print(key2)

    for i in range( int(key1) ):
        answer = answer + str(sorted_l2h[i]) + ', '

    answer = answer[:-2]
    answer = answer + "; "

    for i in range( int(key2) ):
        answer = answer + str(sorted_h2l[i]) + ', '

    answer = answer[:-2]

    print(answer)

    conn.sendline( answer )
    next_question()


def first_question():
    for i in range(11):
        recv = conn.recvline()
        recv = recv.decode('utf-8', 'ignore').strip()
        
        # Get array and sort
        if(i == 8):
            array = recv[9:-1].replace(" ", "").split(',')
            for i in range(0, len(array)): 
                array[i] = int(array[i]) 

            sorted_l2h = sorted(array)
            sorted_h2l = sorted(array, reverse=True)
        
        # Get first key
        if(i == 9):
            key1 = recv[5:]
            
        # Get second key
        if(i == 10):
            key2 = recv[5:]
            
    # Build answer
    answer = ''
    print(array)
    print(sorted_l2h)
    print(sorted_h2l)
    print(key1)
    print(key2)

    for i in range( int(key1) ):
        answer = answer + str(sorted_l2h[i]) + ', '

    answer = answer[:-2]
    answer = answer + "; "

    for i in range( int(key2) ):
        answer = answer + str(sorted_h2l[i]) + ', '

    answer = answer[:-2]

    print(answer)

    conn.sendline( answer )
    next_question()
            
first_question()

# sys.exit()