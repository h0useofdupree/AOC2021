#!/usr/bin/env python3

# Advent of Code 2021, day 1, part 2
# https://adventofcode.com/2021/day/1#part2
# Author: Joel Riekemann
# Date: 2021-12-01

# Read input
with open("../input.txt") as f:
    lines = [int(line.strip()) for line in f]

index = 0
count = 0
clusters = []

# Add trio of numbers to array
for l in lines:
    clusters.append(sum(lines[index:(index + 3)]))
    index += 1
index = 0

for c in clusters:
    if index > 0:
        if clusters[index] > clusters[index - 1]:
            count += 1
    index += 1

print(count)
