#!/usr/bin/env python3

# Advent of Code 2021, day 3, part 1
# https://adventofcode.com/2021/day/3
# Author: Joel Riekemann
# Date: 2021-12-03
# -----------------------------------

from os import device_encoding
import subprocess as sp
from types import resolve_bases

# Read input
with open("../input.txt") as f:
    lines = [line.strip() for line in f]

# gamma
# epsilon
# most_common
# least_common


def copy2clip(txt):
    if type(txt) is not str:
        res = str(txt)
    else:
        res = txt
    cmd = 'echo ' + res.strip() + '| xclip -selection clipboard'
    return sp.check_call(cmd, shell=True)


def decodeInput():
    gamma = []
    epsilon = []

    for pos in range(12):
        count_of_1 = 0
        count_of_0 = 0
        for line in lines:
            if int(line[pos]) == 1:
                count_of_1 += 1
            elif int(line[pos]) == 0:
                count_of_0 += 1
        gamma.append(1 if count_of_1 > count_of_0 else 0)
        epsilon.append(0 if count_of_1 > count_of_0 else 1)
    print(f"""
        Gamma: {gamma}
        Epsilon: {epsilon}
    """)
    gammaStr = "".join(map(str, gamma))
    epsilonStr = "".join(map(str, epsilon))
    return (gammaStr, epsilonStr)


decodedInput = decodeInput()
gammaDec = int(decodedInput[0], 2)
epsilonDec = int(decodedInput[1], 2)

result = gammaDec * epsilonDec
print(f"""
    Gamma in decimal: {gammaDec}
    Epsilon in deciaml: {epsilonDec}
""")
print(result)
copy2clip(result)
