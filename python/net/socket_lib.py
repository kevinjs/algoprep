#!/usr/bin/env python
import socket
from binascii import hexlify

def get_hostname():
    return socket.gethostname()

def get_hostip(hostname=None):
    if hostname:
        return socket.gethostbyname(hostname)
    else:
        return socket.gethostbyname(socket.gethostname())

def convert_ipv4_addr(ip_addr):
    return hexlify(socket.inet_aton(ip_addr))

def get_service_name():
    for port in xrange(1, 10000):
        try:
            print "Port: %s -> %s" %(port, socket.getservbyport(port))
        except socket.error, err_msg:
            #print "Port: %s err_msg: %s" %(port, err_msg)
            pass

if __name__=='__main__':
    #print get_hostip(hostname='www.google.com')
    #print get_hostname()
    #print convert_ipv4_addr('192.168.96.100')

    get_service_name()


    pass
