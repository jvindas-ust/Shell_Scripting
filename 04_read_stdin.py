#!/usr/bin/env python3
import sys

# sys.stdin is a file object. All the same functions that
# can be applied to a file object can be applied to sys.stdin.
for line in sys.stdin.readlines():
	line = line.strip()
	print(line)