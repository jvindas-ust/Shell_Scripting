#!/usr/bin/env python3
import sys

names = {} 
# {
# 	jvindas: 3,
# 	moni: 1
# }

# TODO: search for "authentication failure" and count the times each user has fail
for line in sys.stdin.readlines():
	line = line.strip()
	
	# line = 'asdkfjhasd asldjfh adf jvindas failure'

	#if line.find('failure') >= 0:
	#	print(line)

	if 'failure' in line:
		#cols = line.split() # = ['primera', 'segundas', ... 'n']
		#cols[3]
		
		name = line.split()[3]

		if name in names:
			# names[name] = names[name] + 1
			names[name] += 1
		else:
			names[name] = 1
	

print(names)

	
