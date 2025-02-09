from ftplib import FTP, error_perm
from src.color import color
import sys, os, time

def scan(IP, PORT, f):

    USR = PWD = "anonymous"
    ftp = FTP()
    arr = []
    try:
        try:
            ftp.connect(IP, timeout=5)
            RESPONSE = ftp.login(USR, PWD)
            if RESPONSE == "230 Login successful.":
                f.writelines(f"\n[{time.strftime('%d/%m/%Y')}] Anonymous login work")
                print(f"{color.green}\n[!] System up & anonymous login works {color.reset}")
                print(f"{color.yellow}[+] Files & directory on the FTP server")
                f.writelines(f"\n[{time.strftime('%d/%m/%Y')}] Listing file on the root of the ftp server: \n")
                ftp.retrlines('NLST')
                print()
                ftp.dir()
                ftp.quit()
                f.writelines(f"\n[{time.strftime('%d/%m/%Y')}] Scan successfully done")
                return 0
                
        except error_perm:
            f.writelines(f"\n[{time.strftime('%d/%m/%Y')}] Anonymous login doesn't work, try something else.")
            print(f"{color.red}[!] System up, but anonymous login seems not works {color.reset}")
            return 1

    except KeyboardInterrupt:
        print(f"\n{color.red}[!] Keyboard Interrupt keys pressed ...{color.reset}")
        f.writelines(f"\n[{time.strftime('%d/%m/%Y')}] CTRL+C press")
        sys.exit(0)