#!/usr/bin/env python

import sys
import socket

def reuse_socket_addr():
    local_port = 8787
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))

    srv.listen(1)
    print "listen on port %s" % local_port
    while True:
        try:
            conn, addr = srv.accept()
            print "connect from %s:%s" %(addr[0], addr[1])
        except KeyboardInterrupt:
            #srv.close()
            break
        except socket.error, err_msg:
            print 'Error: %s' % err_msg


if __name__=='__main__':
    reuse_socket_addr()
