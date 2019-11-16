import getpass
import telnetlib

HOST = input("Enter the host you would like to telnet to:")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")

    tn.write(password.encode('ascii') + b"\n")


tn.write("enable\n")
"""
IOS Pops up a warning that vlan databases is being deprecated
While VLAN databases is not encouraged, it sure makes scripting
easier than creating vlans from config mode

"""

for x in range (2, 56):
	tn.write("vlan database" + str(x) + '\n')

tn.write("exit\n")
tn.write("exit\n")
