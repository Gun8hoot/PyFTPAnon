from ftplib import FTP, error_perm
from src.color import color
import sys, os

def scan(IP, PORT, OUTPUT):
    if OUTPUT == None:
        isPath = True
    else:
        isPath = False

    USR = PWD = "anonymous"
    ftp = FTP()
    files = []

    try:
        try:
            ftp.connect(IP, timeout=5)
            RESPONSE = ftp.login(USR, PWD)
            if RESPONSE == "230 Login successful.":
                print(f"{color.green}\n[!] System up & anonymous login works {color.reset}")
                print(f"{color.yellow}[+] Files & directory on the FTP server")
                ftp.dir()
                ftp.quit()
            return 0
        except error_perm:
            print(f"{color.red}[!] System up, but anonymous login seems not works {color.reset}")
    except KeyboardInterrupt:
        print(f"\n{color.red}[!] Keyboard Interrupt keys pressed ...{color.reset}")
        sys.exit