import os,time

banner = r"""______ ___________  ___                    
|  ___|_   _| ___ \/ _ \                   
| |_    | | | |_/ / /_\ \_ __   ___  _ __  
|  _|   | | |  __/|  _  | '_ \ / _ \| '_ \ 
| |     | | | |   | | | | | | | (_) | | | |
\_|     \_/ \_|   \_| |_/_| |_|\___/|_| |_|
        --- SIMILAR TO THE FTP-ANON.NSE ---"""

def log(PATH):
    f = open(PATH, 'w')
    f.write(banner)
    f.write(f"\n\n  ----- LOGS PYFTPANON -----  ")
    f.write(f"\n[!] File create the {time.strftime('%d/%m/%Y')} at {time.strftime('%H:%M:%S')}")
    return

        