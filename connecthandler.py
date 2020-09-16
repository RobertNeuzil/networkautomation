import netmiko
import json


connection_1 = netmiko.ConnectHandler(ip = '192.168.1.1', device_type = 'cisco_ios', username = 'admin', password='robbo12345')

print(connection_1.send_command('sho ip int br'))

connection_1.disconnect()