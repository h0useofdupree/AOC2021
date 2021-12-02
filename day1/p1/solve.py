#!/usr/bin/env python3

# Advent of Code 2021, day 1, part 1
# https://adventofcode.com/2021/day/1
# Author: Joel Riekemann
# Date: 2021-12-01

# Read input into a list of integers
with open("../input.txt") as f:
    numbers = [int(line.strip()) for line in f]


# Output lines
#print(f"Here are the lines: {numbers}")

index = 0
count = 0

# Count every number but the first if it is bigger than the preceding one
for line in numbers:
    if index > 0:
        if line > numbers[index - 1]:
            count += 1
    index += 1
print(count)
