import netmiko
import csv
import datetime
import getpass
from getpass import getpass


deviceid = 1
hosts_path = r'C:\<host IPs path>.txt'
version_path2 = r'C:\<host runconfig saving path>VersionInfo.csv'
username = 'your username'
password = 'your password'

hostfile = open(hosts_path,'r')
content = hostfile.readlines()

with open(version_path2, 'w', newline='') as csvfile:
    data = csv.writer(csvfile)
    data.writerow(['Hostname', 'IP Address', 'OS Version'])

    for i in content:
      print('Device',deviceid,';','Device IP Address:', i)
      net_connect = netmiko.ConnectHandler(ip=i, device_type='cisco_ios', username=username, password=password,port=22)
      hostname = net_connect.send_command('show run | i hostname')
      version = net_connect.send_command('show ver | i Software')
      data.writerow([hostname, i, version])
      print(hostname)
      print(version)
      deviceid = deviceid+1
      net_connect.disconnect()
      print('\n')
    csvfile.close()

print('Show Version Information Collection Done')