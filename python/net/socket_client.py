#!/usr/bin/env python

import sys
import socket
import argparse

host='localhost'

def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print "Connecting to server %s:%s" %(host, port)
    sock.bind(server_address)
    try:
        msg = "test and hello world!"
        print "sending %s" %msg
        sock.sendall(msg)

        amount_received=0
        amount_expected=len(msg)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print 'received: %s' %data
    except socket.error, e:
        print 'socket error: %s' %e
    except Exception, e:
        print 'error :%s' %e
    finally:
        print 'close connection'
        sock.close()



if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Socket server example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port

    #print host, port, ifile
    echo_client(port)

