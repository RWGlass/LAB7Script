import os
from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input('Please enter your Secure Shell username: ')
PASS = getpass('Please enter your Secure Shell password: ')

device = {
  'ip': '',
  'username': USERNAME,
  'password': PASS,
  'device_type': 'cisco_ios'
}

c = ConnectHandler(**device)

output = c.send_command('show run')

f = open('show_run.txt', 'x')

f = write(output)
