#!/usr/bin/env python3

# Advent of Code 2021, day 3, part 2
# https://adventofcode.com/2021/day/3#part2
# Author: Joel Riekemann
# Date: 2021-12-03
# -----------------------------------

import subprocess as sp

# Read input
with open("../input.txt") as f:
    lines = [line.strip() for line in f]


def copy2clip(txt):
    if type(txt) is not str:
        res = str(txt)
    else:
        res = txt
    cmd = 'echo ' + res.strip() + '| xclip -selection clipboard'
    return sp.check_call(cmd, shell=True)


def decodeInput():
    for i in range(2):
        print(len(lines))
        for pos in range(12):
            count_of_1 = 0
            count_of_0 = 0

            for line in lines:
                if int(line[pos]) == 1:
                    count_of_1 += 1
                elif int(line[pos]) == 0:
                    count_of_0 += 0

            if count_of_1 > count_of_0:
                for line in lines:
                    if line.startswith(str(i)) is True:
                        lines.remove(line)
            elif count_of_0 > count_of_1:
                for line in lines:
                    if line.startswith(str(i)) is True:
                        lines.remove(line)
        print(len(lines))
        if i == 0:
            oxyStr = "".join(map(str, lines))
        else:
            co2Str = "".join(map(str, lines))
    return (oxyStr, co2Str)


decodedInput = decodeInput()
oxyDec = int(decodedInput[0], 2)
co2Dec = int(decodedInput[1], 2)

result = oxyDec * co2Dec
print(f"""
    Gamma in decimal: {oxyDec}
    Epsilon in deciaml: {co2Dec}
""")
print(result)
copy2clip(result)
