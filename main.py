import os
from colored import fg, bg, attr
from datetime import *
import platform

appendList = []


def append(path):
    params = path.split(";")
    firstParam = params[0].split(" ")
    appendList.append(firstParam[1])
    for i in params[1::]:
        appendList.append(i) 

    

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
        if command[0:6] == "append":
            append(command)
        else: 
            print(f"{fg('red_1')}Fatal: No command found '{command}'{attr('reset')}")