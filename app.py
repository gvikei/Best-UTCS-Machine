import os
import urllib.request
from bs4 import BeautifulSoup

class Machine:

    def __init__(self, name, status, uptime, n_users, load):
        self.name = name
        self.status = status
        self.uptime = uptime
        self.n_users = n_users
        self.load = float(load)


username = input("Enter your UTCS ID: ")    
machine_list = 'https://apps.cs.utexas.edu/unixlabstatus/'
page = urllib.request.urlopen(machine_list)
soup = BeautifulSoup(page, 'html.parser')

machines = []
items = soup.findAll('td')
for i in range(7,len(items),5):
    name = items[i].text
    status = items[i+1].text
    uptime = items[i+2].text
    n_users = items[i+3].text
    load = items[i+4].text

    if status == 'up':
        machines.append(Machine(name, status, uptime, n_users, load))
    
machines = sorted(machines, key=lambda x: (x.load, x.n_users))
print ('Best machine to logon to:', machines[0].name)

os.system('ssh {}@{}.cs.utexas.edu'.format(username, machines[0].name))