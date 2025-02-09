#!/bin/python3

from ftplib import FTP, error_perm
import os, sys, time
from src.color import color
from src.argmuents import arguments
from src.FTPScan import scan
from src.getHelp import getHelp
from src.checkVersion import checkVersion
from src.logsCreation import log

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
    global LOG
    print(color.purple , banner, color.reset)
    IP, PORT, PATH = arguments()
    LOG = log(PATH, banner)
    checkVersion()
    isFinish = scan(IP, PORT, LOG)
    if isFinish == 0 or isFinish == 1:
        LOG.writelines(f"\n[{time.strftime('%d/%m/%Y')}] Scan succesfully done")
        sys.exit(0)
    else:
        LOG.writelines(f"\n[{time.strftime('%d/%m/%Y')}] ERROR")
        print("[!] Wwhoops, somethings goes wrong")
        sys.exit(0)
    
if __name__ == "__main__":
    main()

