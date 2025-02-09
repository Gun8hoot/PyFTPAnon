# PyFTPAnon
Lightweight **anonymous credential detector** who use the build-in python3 library called **ftplib**. If the victim have anonymous connection settings enable, the script will **list all file on the ftp root directory**.
> The output function is currently not available
## TODO
- [  ] Listing every files on the ftp server
## INSTALLATION AND USAGES
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
sudo python3 ./main.py -i/-I {IP ADDRESS} -p/-P {PORT NUMBER} -o/-O {NAME OF THE OUTPUT FILE}
# 2nd
chmod u+x ./main.py
sudo ./main.py -i/-I {IP ADDRESS} -p/-P {PORT NUMBER} -o/-O {NAME OF THE OUTPUT FILE}
```

 
