#!/usr/bin/env python3
# Author: Sourav
# Author ID: 156533226
# Date Created: 2025/02/07

import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Extract arguments
name = sys.argv[1]
age = sys.argv[2]

# Output the result
print(f"Hi {name}, you are {age} years old.")
