##from pandas import *
import json
import csv
packages=[]
malware=[]

##data=read_csv("pkgs.csv", delimiter=',')

data_csv = csv.reader("pkgs.csv")
for row in data_csv:
    malware.append(row)

with open('output.json', mode='r') as f:
    data_json=json.load(f)

for j in data_json:
    packages.append(j['name'])

deinstall=[]

for item1 in packages:
    for item2 in malware:
        if item1 == item2:
            deinstall.append(item1)
        else:
            continue
if len(deinstall) == 0:
    print("No malicious packages were found") 
else:
    print("The following packages {} should be immeadiately deinstalled".format(deinstall))