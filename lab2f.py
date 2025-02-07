#!/usr/bin/env python3
# Author: Sourav
# Author ID: 156533226
# Date Created: 2025/02/07

import sys

# Check if the correct number of arguments are provided (at least 1 argument besides the script name)
if len(sys.argv) == 1:  # No arguments besides the script name
    print(f"Usage: {sys.argv[0]} <number>")
    sys.exit(1)  # Exit with status code 1 to indicate error

# Get the number from the first argument
try:
    countdown_number = int(sys.argv[1])
except ValueError:
    print(f"Invalid input: {sys.argv[1]} is not a valid number.")
    sys.exit(1)

# Perform the countdown
while countdown_number > 0:
    print(countdown_number)
    countdown_number -= 1

# Print "blast off!" when countdown finishes
print("blast off!")
