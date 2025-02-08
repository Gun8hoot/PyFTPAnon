# PyFTPAnon
Lightweight anonymous credential detector who work with the build-in python3 library called ftplib. If the victim have anonymous connection settings, the script will list all file on the ftp root directory.
> ⚠️ **Notes :** The output option is currently not available (bugged asf)
---
- You need python3 on your computer 
```bash
sudo apt install python3 
```
- Clone the repository from Github
```bash
git clone https://github.com/Gun8hoot/PyFTPAnon.git
```
- Go to the repository
```bash
cd ./PyFTPAnon
```
- Execute the script (2 possibilities)
```bash
# 1st
sudo python3 ./main.py -i {IP ADDRESS} -o {NAME OF THE FILE}
# 2nd
chmod u+x ./main.py
sudo ./main.py -i {IP ADDRESS} -o {NAME OF THE FILE }
```

---
 
