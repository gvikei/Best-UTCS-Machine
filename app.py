import os
import urllib.request
from bs4 import BeautifulSoup

'''
Class for defining one lab machine
'''
class Machine:
    def __init__(self, name, status, uptime, n_users, load):
        self.name = name
        self.status = status
        self.uptime = uptime
        self.n_users = n_users
        self.load = float(load)

# Init
username = input("Enter your UTCS ID: ")    
machine_list = 'https://apps.cs.utexas.edu/unixlabstatus/'
page = urllib.request.urlopen(machine_list)
soup = BeautifulSoup(page, 'html.parser')

# Parse
machines = []
N_HEADING_LINES = 7
N_ITEMS = 5

items = soup.findAll('td')
for i in range(N_HEADING_LINES, len(items), N_ITEMS):
    name = items[i].text
    status = items[i+1].text
    uptime = items[i+2].text
    n_users = items[i+3].text
    load = items[i+4].text
    
    if status == 'up':
        machines.append(Machine(name, status, uptime, n_users, load))

# Sort by smaller load time, then smaller number of current users   
machines = sorted(machines, key=lambda x: (x.load, x.n_users))
print ('---------------------------------------')
print ('Best machine to logon to:', machines[0].name)
print ('Load time: {} | Number of users: {}'.format(machines[0].load, machines[0].n_users))
print ('---------------------------------------')

os.system('ssh {}@{}.cs.utexas.edu'.format(username, machines[0].name))