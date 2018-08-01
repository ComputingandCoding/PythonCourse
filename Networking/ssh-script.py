#!/usr/bin/ene python

from netmiko import ConnectHandler

iosv_l2 = {
		'device':'cisco_ios',
		'ip':'1.1.1.1',
		'username':'abc'
		'password':'abc'
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print(output)

config_command = ['int loop 0', 'ip address 1.1.1.1 255.255.255.255']
output = net_connect.send_command(config_command)
print(output)

for n in range (2,11):
	print("Creating VLAN " + str(n))
	config_command = ['vlan ' + str(n), 'name dynamic_VLAN' + str(n)]
	output = net_connect.send_command(config_command)
	print(output)
# you can use python process pool for speed thing up