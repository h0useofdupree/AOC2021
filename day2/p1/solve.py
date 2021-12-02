#!/usr/bin/env python3

# Advent of Code 2021, day 2, part 1
# https://adventofcode.com/2021/day/2
# Author: Joel Riekemann
# Date: 2021-12-02
# -----------------------------------

import time as t
import subprocess as sp
import sys


def copy2clip(txt):
    cmd = 'echo '+txt.strip()+'| xclip -selection clipboard'
    return sp.check_call(cmd, shell=True)


# Read input
with open("../input.txt") as f:
    lines = [line.strip() for line in f]
# Instruction format is <direction> <value>

hPos = 0
vPos = 0

if "slow" in sys.argv:
    slow = True
else:
    slow = False

for l in lines:
    # Split line at " " to separate direction and value
    instruction = l.split(" ")
    # Based on input, decide wether to add / subtract from hPos / vPos
    if instruction[0] == "up":
        vPos -= int(instruction[1])
    elif instruction[0] == "down":
        vPos += int(instruction[1])
    elif instruction[0] == "forward":
        hPos += int(instruction[1])
    print(f"""
        Direction: {instruction[0]}
        Value: {instruction[1]}
        vPos now is: {vPos}
        hPos now is: {hPos}
    """)
    if slow:
        t.sleep(.1)

result = vPos * hPos

print(f"""
    Vertical Position: {vPos}
    Horizontal Position: {hPos}
    Both multiplied: {result}
""")
copy2clip(str(result))
