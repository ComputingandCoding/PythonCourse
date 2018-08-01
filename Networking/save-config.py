# script for multiple devices , Devises IP's are 
#stored in txt file


import getpass
import sys
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

f =open("IP.txt")

for IP in f:
	IP = IP.strip() # strip any space after the IP 
	print("Get Running Config " + (IP))
	HOST = IP  # ip address of the device to connect to
	tn = telnetlib.Telnet(HOST)
	tn.read_until(b"Username: ") # will read what is on the screen login or username 
	tn.write(user.encode('ascii') + b"\n")
	if password:
    	tn.read_until(b"Password: ")
    	tn.write(password.encode('ascii') + b"\n")
	tn.wriet(b"terminal length 0\n")
	tn.write(b"show run\n")
	tn.write(b"exit\n")

	readoutput = tn.read_all()
	saveoutput = open("Switch" + HOST , "w")
	saveoutput.write(readoutput.decode("ascii"))
	saveoutput.write("\n")
	saveoutput.close
	print(tn.read_all().decode("ascii"))




