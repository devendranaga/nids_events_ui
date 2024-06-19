#!/usr/bin/python3

# implements the udp server

import socket

class UdpServer:
    def init(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))

    def get_data(self):
        msg, addr = self.sock.recvfrom(1024 * 10)
        return msg

