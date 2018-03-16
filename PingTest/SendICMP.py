# coding=utf-8
import ctypes
import os
import socket

def checkIsAdmin():
    try:
        return ctypes.windll.winshell32.IsUserAnAdmin()
    except:
        return False
"""
这通常出现在RAW Socket请求的代码中。Packet的header中需要一个唯一ID，
通常就用当前进程的PID了。但这个id是要求unsigned short(16 bit)，所以就取os.Getpid()&0xffff了。
"""
my_ID = os.getpid() & 0xFFFF
icmp = socket.getprotobyname('icmp')
my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)