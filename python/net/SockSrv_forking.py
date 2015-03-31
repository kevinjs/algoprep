#!/usr/bin/env python

import os
import sys
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024
ECHO_MSG = 'Hello server!'

class ForkingClient(object):
    def __init__(self, ip, addr):
	#create socket (tcp)
	self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, addr))

    def run(self):
	cur_pid = os.getpid()
	print 'Current processing: %s, send message: %s' %(cur_pid, ECHO_MSG)
	send_data_len = self.sock.send(ECHO_MSG)
	print 'Send %s char' % send_data_len

	resp = self.sock.recv(BUF_SIZE)
	print 'PID: %s received: %s' %(cur_pid, resp[:])

    def shutdown(self):
	self.sock.close()


class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
	data = self.request.recv(BUF_SIZE)
	cur_pid = os.getpid()
	resp = '%s: %s' %(cur_pid, data)
	print 'Server sending response: %s' %resp
	self.request.send(resp)
	return

class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer,):
    pass 

def main():
    # tell kernel to choose port randomly
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.server_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    print 'Server loop running PID: %s' %os.getpid()

    c1 = ForkingClient(ip, port)
    c1.run()

    c2 = ForkingClient(ip, port)
    c2.run()

    server.shutdown()
    c1.shutdown()
    c2.shutdown()
    server.socket.close()

if __name__=='__main__':
    main()

