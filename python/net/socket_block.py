#!/usr/bin/env python

import socket

def test_socket_modes():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, err_msg:
        print "Create socket error: %s" %err_msg

    s.setblocking(0)
    s.settimeout(0.5)
    s.bind(('127.0.0.1', 0))

    socket_addr = s.getsockname()
    print 'launched on socket: %s' %str(socket_addr)

    while True:
        s.listen(1)

if __name__=='__main__':
    test_socket_modes()
