#!/usr/bin/env python

import os
import sys
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024

def client(ip, port, msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
	sock.sendall(msg)
	resp = sock.recv(BUF_SIZE)
	print 'Client received: %s' %resp
    finally:
	sock.close()

class ThreadingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
	data = self.request.recv(BUF_SIZE)
	cur_thread = threading.current_thread()
	resp = '%s: %s' %(cur_thread, data)
	self.request.sendall(resp)

class ThreadingServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer,):
    pass 

def main():
    # tell kernel to choose port randomly
    server = ThreadingServer((SERVER_HOST, SERVER_PORT), ThreadingServerRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    print 'Server loop running thread: %s' %server_thread.name

    client(ip, port, "asdf111")
    client(ip, port, "we will rock you")
    client(ip, port, "Hotel california")

    server.shutdown()

if __name__=='__main__':
    main()

