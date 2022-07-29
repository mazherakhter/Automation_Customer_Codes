import netmiko
from netmiko import ConnectHandler
import datetime
import os

deviceid = 1
hosts_path = r"C:\<host IPs path>.txt"
rc_path2 = r"C:\<host runconfig saving path>RC_"
time = str(datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
username = 'your username'
password = 'your password'

hostfile = open(hosts_path, 'r')
content = hostfile.read().split()

for i in content:
    print('Device', deviceid, ';', 'Device IP Address:', i, '...')
    net_connect = netmiko.ConnectHandler(ip=i, device_type='cisco_ios', username=username, password=password, port=22)
    net_connect.send_command('ter len 0')
    output = net_connect.send_command('show run')
    myfile = open(rc_path2+i+'_'+time+'.txt','w')
    myfile.write(output)
    myfile.close()
    print('Device', i, 'Done')
    net_connect.disconnect()
    deviceid = deviceid + 1

print('Session Disconnected')
