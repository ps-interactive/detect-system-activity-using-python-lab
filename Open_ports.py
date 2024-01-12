import subprocess
from datetime import date

Port_Number = str(input("What port numbers should be open? Please use the following format. E.G 22/tcp 23/udp 24/tcp "))
Approved_list = Port_Number.split()
print(Approved_list)

# Full script for gathering open ports
open_ports = subprocess.run(["sudo nmap -sT -O localhost | grep -w \"open\""], shell=True, capture_output=True, text=True)
raw_ports = str(open_ports.stdout)
list = raw_ports.split()
matches = []
for i in list:
    if "/" in i:
        matches.append(i)
print(matches)

# Comparison

Unauthorized_Ports = []

for i in matches:
    if i not in Approved_list:
        Unauthorized_Ports.append(i)

if Unauthorized_Ports != []:
    file1 = open('security.log', 'a')
    alert = 'Unauthorized ports were opened, please check nmap!!! '
    today = date.today()
    str_date = ' ' + str(today) + '\n'
    Ports = ', '.join(Unauthorized_Ports)
    file1.write(alert)
    file1.write(Ports)
    file1.write(str_date)
    file1.close()