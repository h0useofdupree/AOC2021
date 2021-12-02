#!/usr/bin/env python3

# Advent of Code 2021, day 2, part 1
# https://adventofcode.com/2021/day/2
# Author: Joel Riekemann
# Date: 2021-12-02

# Read input
with open("../input.txt") as f:
    lines = [line.strip() for line in f]

# Output instructions
print(lines)

# Instruction format is <direction> <value>
# Now add those to a dict with separate 'direction' and 'value' fields
seperatedInstructions = {
    "direction":
    "value": }
for l in lines:
    seperatedInstructions
