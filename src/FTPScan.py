from ftplib import FTP, error_perm
from src.color import color
import sys, os, time

def scan(IP, PORT, OUTPUT):
    if OUTPUT == None:
        isPath = True
    else:
        isPath = False

    USR = PWD = "anonymous"
    ftp = FTP()
    f = open(PATH, 'w')

    try:
        try:
            ftp.connect(IP, timeout=5)
            RESPONSE = ftp.login(USR, PWD)
            if RESPONSE == "230 Login successful.":
                f.write(f"[{time.strftime('%d/%m/%Y')}] Anonymous login work")
                print(f"{color.green}\n[!] System up & anonymous login works {color.reset}")
                print(f"{color.yellow}[+] Files & directory on the FTP server")
                f.write(f"[{time.strftime('%d/%m/%Y')}] Listing file on the root of the ftp server: ")
                f.write(ftp.dir())
                ftp.dir()
                ftp.quit()
            return 0
        except error_perm:
            f.write(f"[{time.strftime('%d/%m/%Y')}] Anonymous login does not work, try something else")
            print(f"{color.red}[!] System up, but anonymous login seems not works {color.reset}")
    except KeyboardInterrupt:
        print(f"\n{color.red}[!] Keyboard Interrupt keys pressed ...{color.reset}")
        f.write(f"[{time.strftime('%d/%m/%Y')}] CTRL+C press")
        sys.exit(0)