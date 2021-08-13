import os

os.system("pip install scapy")
os.system("pip install colored")
os.system('cls||clear')

import scapy.all as scapy
from colored import fg,attr

def colorprint(text,color):
	print("%s{}%s".format(text) % (fg(color), attr(0)))

while True:
	ip = input("[SYSTEM] Plese enter ip address [EX: 192.168.1.0/24]: ")

	if "/24" not in ip and "/16" not in ip and "/8" not in ip:
		colorprint("\n[SYSTEM] There is an error in the ip you entered, please enter a correct ip.\n",1)
		continue
		
	else: break

arp = scapy.ARP(pdst=ip)
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
combine = broadcast/arp
(alist,ualist) = scapy.srp(combine,timeout=1,verbose=0)

print(f"""
Machine IP: {combine.psrc}
Machine MAC Address: {combine.hwsrc.upper()}
---------------------------------------
IP: {str(alist[0][1].psrc)}     MAC: {str(alist[0][1].hwsrc.upper())}""")

for i in range(1,1000):
	try:
		print(f"IP: {str(alist[i][1].psrc)}   MAC: {str(alist[i][1].hwsrc.upper())}")
	except IndexError:
		pass
