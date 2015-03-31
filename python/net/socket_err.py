#!/usr/bin/env python

import sys
import socket
import argparse

def set_buff_size():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    buf_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print 'Buffer size: %d' %buf_size

def err_test(host, port, ifile):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, err_msg:
        print "Error creating socket: %s" %err_msg
        sys.exit(1)

    try:
        s.connect((host, port))
    except socket.gaierror, err_msg:
        print "Address error connecting to: %s" %err_msg
        sys.exit(1)
    except socket.error, err_msg:
        print "Connection error: %s" %err_msg
        sys.exit(1)

    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n" %ifile)
    except socket.error, err_msg:
        print "Send data error: %s" %err_msg
        sys.exit(1)

    while True:
        try:
            buf = s.recv(2048)
        except socket.error, err_msg:
            print "Error receiving data: %s" % err_msg
            sys.exit(1)

        if not len(buf):
            break
        sys.stdout.write(buf)



if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Socket error test')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    ifile = given_args.file

    #print host, port, ifile
    err_test(host, port, ifile)

