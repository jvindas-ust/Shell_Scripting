#!/usr/bin/env python3

import os

print(os.environ['HOME'])


# Create a value for the current session only because
# you can't change your shell's environment from a child process such as Python
os.environ['APP_TOKEN'] = '1234567890'
print(os.environ.get('APP_TOKEN'))

# For code robustness use get to provide a default value and avoid errors
print(os.environ.get('APP_SECRET', 'Not Set'))