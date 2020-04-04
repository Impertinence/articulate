
#ExclamationAI written by Pranav Hegde

import socket
import sqlite3
import os
import hashlib
import threading
import time
import random

import netifaces as ni

from threading import Thread
from uuid import getnode as get_mac
from socketserver import ThreadingMixIn

BUFFER_SIZE = 20
transmit_port = 1980

#Connect to db
conn = sqlite3.connect('dbs/main.db')
c = conn.cursor()

#Devices
devices = []

#Exclamation products on network
products = []

#Global
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ni.ifaddresses('eth0')
my_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

#Send a message to device
def send_message(host, port, message):
        tcpClient.connect((host, int(port)))
        tcpClient.send(bytes(message))

#Get devices currently on network
def getDevices():
        split_addr = my_ip.split('.')
        base_addr = split_addr[0] + "." + split_addr[1] + "." + split_addr[2]

        for ping in range(1, 300):
                address = base_addr + "." + str(ping)
                print(address)

getDevices()

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
        def __init__(self,ip,port):
                Thread.__init__(self)
                self.ip = ip
                self.port = port
                print ("[+] New server socket thread started for " + ip + ":" + str(port))

        def run(self):
                while True:
                        data = str(conn.recv(2048), "utf-8")
                        print(data)

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = 4444
BUFFER_SIZE = 20  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
        tcpServer.listen(4)
        print ("[+] Waiting for jobs...")
        (conn, (ip,port)) = tcpServer.accept()
        newthread = ClientThread(ip,port)
        newthread.start()
        threads.append(newthread)

for t in threads:
        t.join()




