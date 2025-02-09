import os,time

def log(PATH, banner):
        if PATH == None:
                f = open("/dev/null", 'w')
        elif PATH != None:
                f = open(PATH, 'w')
                f.writelines(banner)
                f.writelines(f"\n\n  ----- LOGS PYFTPANON -----  ")
                f.writelines(f"\n[!] File create the {time.strftime('%d/%m/%Y')} at {time.strftime('%H:%M:%S')}")
        return f