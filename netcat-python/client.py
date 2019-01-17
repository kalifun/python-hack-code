# -*- coding:utf-8 -*-
import sys
import socket


def create_socket(socket_ip,socket_port):
    conn = socket.socket()
    conn.connect((str(socket_ip),int(socket_port)))
    get_bytes = conn.recv(1024)
    get_info = str(get_bytes)
    print get_info
    while True:
        try:
            sed_data = raw_input(">>>")
            if sed_data == "q":
                conn.send(bytes(sed_data))
                break
            else:
                try:
                    conn.send(bytes(sed_data))
                    get_bytes = conn.recv(1024)
                    get_info = str(get_bytes)
                    print get_info
                except Exception,e:
                    print "Command Not Found !"
                    create_socket(socket_ip,socket_port)
                    # sed_data = raw_input(">>>")
                    # conn.send(bytes(sed_data))
                    # get_bytes = conn.recv(1024)
                    # get_info = str(get_bytes)
                    # print get_info
        except Exception,e:
            print e


if __name__ == "__main__":
    socket_ip = sys.argv[1]
    socket_port = sys.argv[2]
    create_socket(socket_ip,socket_port)