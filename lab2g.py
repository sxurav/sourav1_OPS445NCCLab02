#!/usr/bin/env python3

# Author: Sourav
# Author ID: 156533226
# Date Created: [2025/02/07]

import sys

# Default value for timer is 3
timer = 3

if len(sys.argv) > 1:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
