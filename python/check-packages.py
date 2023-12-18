##from pandas import *
import json
import csv
packages=[]
malware=[]

##data=read_csv("pkgs.csv", delimiter=',')

with open('malware_list.json', mode='r') as f1:
    malware_dict=json.load(f1)

##for (i, j) in malware_dict:
##    malware.append(['name'])

with open('output.json', mode='r') as f2:
    packages_dict=json.load(f2)

##for j in packages_dict:
##    packages.append(j['name'])


deinstall=[]

for item1 in packages_dict:
    for item2 in malware_dict:
        if item1['name'] == item2['name']:
            deinstall.append(item2)
        else:
            continue

if len(deinstall) == 0:
    print("No malicious packages were found") 
else:
    print("The following packages {} should be immeadiately deinstalled".format(deinstall))
