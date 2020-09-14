#Rafael Esmundo 1/24/2020
#phython3
#Aruba Mobility Show commands

#using netmiko
from netmiko import ConnectHandler

#Used device 3810; Have not found a reference for MC
A3810_1 = {
	'device_type': 'hp_procurve',
    'host':   'x.x.x.x',
    'username': 'xxxxx',
    'password': 'xxxxx',
}

#connect to MC
net_connect = ConnectHandler(**A3810_1)

#Run Show commands
output1 = net_connect.send_command("show ip interface brief")


#Print show commands to screen
print(output1)
