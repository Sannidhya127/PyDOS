import os
from colored import fg, bg, attr
from datetime import *
import platform
import psutil
import socket
from getmac import get_mac_address as gma

appendList = []


def append(path):
    params = path.split(";")
    firstParam = params[0].split(" ")
    appendList.append(firstParam[1])
    for i in params[1::]:
        appendList.append(i) 


def arp():
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            # print(f"=== Interface: {interface_name} ===")
            macAdd = gma()
            if str(address.family) == 'AddressFamily.AF_INET':
                # print(f"  IP Address: {address.address}")
                # print(f"  Netmask: {address.netmask}")
                # print(f"  Broadcast IP: {address.broadcast}")
                output = f'''   Interface: {interface_name}
                Internet Address    Physical Adress    Type
                {address.address}      {macAdd}     {socket.SO_TYPE}'''
                print(output)
          
if __name__ == '__main__':
    exitCommands = ['exit', 'q', 'quit', 'pydos --q', 'exit()']
    current_directory = os.getcwd()
    device_name = platform.node()
    timeNow = datetime.now()
    initiation = f'''{fg('green_1')}    PyDOS v.ALPHA
    Developed by Sannidhya127 with coffee in python
    
    Computer {device_name}
    Current Time = {timeNow}
                    
                   {attr('reset')} '''

    print(initiation)
    while True:
        command = input(f"PyDOS prompt {current_directory}>")
        if command in exitCommands:
            exit()
        elif command[0:6] == "append":
            append(command)
        elif command == "arp":
            arp()
        else: 
            print(f"{fg('red_1')}Fatal: No command found '{command}'{attr('reset')}")