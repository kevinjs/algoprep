#!/usr/bin/env python

import socket

SEND_BUF_SIZE=9192
RECV_BUF_SIZE=9192

def set_buff_size():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    buf_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print 'Buffer size: %d' %buf_size

    #s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    #s

if __name__=='__main__':
    set_buff_size()
