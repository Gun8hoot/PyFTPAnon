#!/bin/env python3

from ftplib import FTP, error_perm
from scapy import *
import argparse, os, sys

#   COLOR CLASS
class color():
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    purple = "\x1b[38;5;5m"
    # ---
    reset = "\x1b[00m"

#   BANNER
banner = """______ ___________  ___                    
|  ___|_   _| ___ \/ _ \                   
| |_    | | | |_/ / /_\ \_ __   ___  _ __  
|  _|   | | |  __/|  _  | '_ \ / _ \| '_ \ 
| |     | | | |   | | | | | | | (_) | | | |
\_|     \_/ \_|   \_| |_/_| |_|\___/|_| |_|
        --- SIMILAR TO THE FTP-ANON.NSE ---"""


#   ARGUMENT & VARS
parser = argparse.ArgumentParser(prog="FTP_ANON")
parser.add_argument('-i', '--ip', dest='ip', help=f'[{color.red}REQUIRED{color.reset}] Specify the ip address', required=True)
parser.add_argument('-o', '--output', dest='file', help=f'[{color.yellow}OPTIONAL{color.reset}] Specify the file output', required=False)
args = parser.parse_args()
#   --- 
i_p = args.ip
out_put = None #args.file TODO
#   ---


#   FUNCTION
def output_file(aaa):
    path = "./"
    filename = strftime("FTPAnonScan %H:%M:%S %d %m %Y.txt")
    f = open(filename, w+x)
    f.write(aaa)
    
def pinging(ip):
    print("\nTODO\n")
    pass

def connect(ip,file):
    if file != None or file == None:
        print(f"{color.red}[!] The output option is currently not available.{color.reset}")
    else:
        pass

    USR = PWD = "anonymous"
    ftp = FTP()
    try:
        try:
            ftp.connect(ip, timeout=5)
            RESPONSE = ftp.login(USR, PWD)
            if RESPONSE == "230 Login successful.":
                print(f"{color.green}[!] System up & anonymous login works {color.reset}\n")
                print(f"{color.yellow}[+] Files & directory on the FTP server")
                ftp.dir()
                ftp.quit()
            return
        except error_perm:
            print(f"{color.red}[!] System up, but anonymous login seems not works {color.reset}\n")
    except KeyboardInterrupt:
        print(f"\n{color.red}[!] Keyboard Interrupt keys pressed ...{color.reset}")
        sys.exit

#   MAIN
if __name__ == '__main__':
    print(color.purple + banner + color.reset)
    aaa = connect(i_p, out_put)
else:
    print(f"{color.red}[!] FATAL_ERROR{color.reset}")
