import os
import datetime
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import SSHException
from netmiko.ssh_exception import NetMikoTimeoutException

USERNAME = input('Please enter your Secure Shell username: ')

PASS = getpass('Please enter your Secure Shell password: ')

device = {
  'ip': '192.168.108.10',
  'username': USERNAME,
  'password': PASS,
  'device_type': 'cisco_ios'
}

try:
	c = ConnectHandler(**device)
	output = c.send_command('show run')
	f = open('show_run.txt', 'x')
	f.write(output)
	f.close()
except (AuthenticationException):

    print("An authentication eror occured when connecting to: " + device['ip'])

except (SSHException):

    print("An SSH error occured when connecting to:" + device['ip'])

except (NetMikoTimeoutException):

    print("A timeout error occured when connecting to:" + device['ip'])
