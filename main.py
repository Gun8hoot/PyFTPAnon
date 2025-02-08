#!/bin/python3

from ftplib import FTP, error_perm
import os, sys, time
from src.color import color
from src.argmuents import arguments
from src.FTPScan import scan
from src.getHelp import getHelp
from src.checkVersion import checkVersion

# --- BANNER ---
banner = r"""______ ___________  ___                    
|  ___|_   _| ___ \/ _ \                   
| |_    | | | |_/ / /_\ \_ __   ___  _ __  
|  _|   | | |  __/|  _  | '_ \ / _ \| '_ \ 
| |     | | | |   | | | | | | | (_) | | | |
\_|     \_/ \_|   \_| |_/_| |_|\___/|_| |_|
        --- SIMILAR TO THE FTP-ANON.NSE ---"""


# --- RUN ---
def main():
    try:
        print(color.purple , banner, color.reset)
        IP, PORT, PATH = arguments()
        if PATH != None:
            f = open(PATH, 'w')
        elif PATH == None:
            pass
        checkVersion()
        isFinish = scan(IP, PORT, PATH)
        if isFinish == 0:
            f.write(f"[{time.strftime('%d/%m/%Y')}] Scan finish!")
            print(f"{color.green}[+] Scan succesfully done {color.reset}")
        else:
            f.write(f"[{time.strftime('%d/%m/%Y')}] ERROR")
            print("[!] Wwhoops, somethings goes wrong")
    except:
        f.write(f"[{time.strftime('%d/%m/%Y')}] Enter a correct IP address")
        print(color.red, "[!] You need to specify the IP address to attack", color.reset)
        sys.exit(0)
    
if __name__ == "__main__":
    main()

