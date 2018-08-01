#!/usr/bin/ene python

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
