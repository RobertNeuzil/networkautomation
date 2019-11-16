'''
A small python script that will telnet into a router and change it's
hostname to TYLER_DURDEN
and then close the telnet connection 
'''

import getpass
import telnetlib

client_ip = input("Enter the client you would like to telnet to:")
username = input( "Enter the username you will use")
password = getpass.getpass()   ''' cisco '''
enable_secret = tomjohnson

def begin_telnet():

	telnetlib.Telnet(client_ip)
	telnetlib.read_until(b"Password: ")
	telnetlib.write(password.encode('ascii') + b"\n")
	telnetlib.write(b"enable\n")
	telnetlib.write(enable_secret.encode('ascii') + b"\n")
	telnetlib.write(b"configure terminal\n")
	telnetlib.write(b"hostname TYLER_DURDEN\n")
	telnetlib.write(b"exit")
	telnetlib.write(b"copy running-config startup-config\n")
	#Could not understand what the problem was. Cisco's IOS prompts you to confirm you're sure you want to copy run start
	telnetlib.write(b"\n")
	#close the telnet connection
	telnet.write(b"exit\n")


begin_telnet()