#!/usr/bin/ene python



'''
Netmiko - Multi-Vendor library to simplify Paramiko SSH connections to network devices
more information on github - Netmiko page

Check if SSH is enable on devices
1- configure devices to support SSH
ssh abc@1.1.1.1   - port 22 should be open on devices

If Not then use the below commands to configure SSH On devices

#username abc pass abc
#usernmae abc priv 15
#line vty 0 4
##login local
##transport input all
#ip domain-name ccie.com
#crypto key generate rsa 1024

#sh ssh
#

'''

from netmiko import ConnectHandler

iosv_l2_s1 = {
		'device':'cisco_ios',
		'ip':'1.1.1.1',
		'username':'abc'
		'password':'abc'
}

iosv_l2_s2 = {
		'device':'cisco_ios',
		'ip':'1.1.1.1',
		'username':'abc'
		'password':'abc'
}

iosv_l2_s3 = {
		'device':'cisco_ios',
		'ip':'1.1.1.1',
		'username':'abc'
		'password':'abc'
}

all_devices = [iosv_l2_s1,iosv_l2_s2,iosv_l2_s3]

for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	for n in range(2,21):
		print("Creating VLAN " + str(n))
		config_commands = ['vlan ' + str(n), 'name dynamic_VLAN' + stv(n)]
		output = net_connect.send_config(config_commands)
		print(output)

#to configure commands from the file 

with open('abc.txt') as f:
	lines = f.read().splitilines()
	print(lines)

for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	output = net_connect.send_config(lines)
	print(output)
