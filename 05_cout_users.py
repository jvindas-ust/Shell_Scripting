#!/usr/bin/env python3
import sys

names = {}
for line in sys.stdin.readlines():
	line = line.strip()
	# TODO: search for "authentication failure" and count the times each user has fail
