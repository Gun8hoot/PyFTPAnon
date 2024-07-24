# PyFTPAnon
Lightweight anonymous credential detector who work with the build-in python3 library called ftplib. If the victim have anonymous connection settings, the script will list all file on the ftp root directory.
> ⚠️ **Notes :** The output option is currently not available
## Windows
Not test
## Linux
- You need python3 on your computer 
```shell
sudo apt install python3 # on debian
# ---
sudo pacman -Sy python-pip # on arch
```
- Clone the repository from Github
```shell
git clone https://github.com/Gun8hoot/PyFTPAnon.git
```
- Go to the repository
```shell
cd ./PyFTPAnon
```
- Execute the script (2 possibilities)
```shell 
# 1st
sudo python3 ./main.py -i {IP ADDRESS} -o {NAME OF THE FILE}
# 2nd
chmod u+x ./main.py
sudo ./main.py -i {IP ADDRESS} -o {NAME OF THE FILE }
```
> 💡 **Notes :**  To attack VM host in your computer you didn't need ***sudoers privileges***

---
 
