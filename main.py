from ftplib import FTP, error_perm
import os, sys
from src.color import color
from src.argmuents import arguments
from src.FTPScan import scan
from src.getHelp import getHelp

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
        isFinish = scan(IP, PORT, PATH)
        if isFinish == 0:
            print(f"{color.green}[+] Scan succesfully done{color.reset}")
        else:
            print("whoops, somethings goes r")
    except:
        pass
    
if __name__ == "__main__":
    main()

