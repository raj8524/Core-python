print("hellow")

from netmiko import ConnectHandler
import getpass
import sys
p = getpass.getpass(stream=sys.stderr)
# p=getpass.getpass()
cisco_device={
    'device_type':'cisco_ios',
    'host':'10.8.243.61',
    'username':'admin.raj',
    'password':p,
    'port':22,
    'secret':'cisco',
    'verbose':True
    }
connection=ConnectHandler(**cisco_device)
output=connection.send_command('show ip int bri')
print(output)
connection.enable()
prompt=connection.find_prompt()
print(prompt)
# connection.config_mode()
# print(connection.check_config_mode())
print("closing connection")
connection.disconnect()
