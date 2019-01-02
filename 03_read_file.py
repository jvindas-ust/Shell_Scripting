#!/usr/bin/env python3

with open('days.txt') as file:
    for line in file:
    	# Each line will have a newline on the end
        # that should be removed.
        line = line.strip()
        print(line)

