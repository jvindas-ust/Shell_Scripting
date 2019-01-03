#!/usr/bin/env python3
import sys, json
import collections as col
names = {}
nombre=[]

for line in sys.stdin.readlines():
        line = line.strip()
        if 'authentication failure' in line:
                nombre.append((line.split()[3]))
names=col.Counter(nombre)

with open('user_data.json', 'w+') as fl:
        fl.write(json.dumps(names))
        #fl.write(json.dumps(names), sort_keys=True, indent=4, separators=(',', ': ')).encode("utf-8"))

# TODO: search for "authentication failure" and count the times each user has fail
~
~
~
~
