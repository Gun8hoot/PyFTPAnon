import os, requests

def checkVersion():
    with open("./version", "r") as v:
        v = v.read()
    r = requests.get('https://raw.githubusercontent.com/Gun8hoot/PyFTPAnon/refs/heads/main/version')
    print(r.content)
    
    