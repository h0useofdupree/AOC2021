#!/usr/bin/env python3

# Advent of Code 2021, day 3, part 2
# https://adventofcode.com/2021/day/3#part2
# Author: Joel Riekemann
# Date: 2021-12-03
# -----------------------------------

import subprocess as sp
import sys


def readInput():
    # Read input
    with open("/home/juuls/Documents/aoc/day3/input.txt") as f:
        lines = [line.strip() for line in f]
    return lines


# Copy result to clipboard
def copy2clip(txt):
    if type(txt) is not str:
        res = str(txt)
    else:
        res = txt
    cmd = 'echo ' + res.strip() + '| xclip -selection clipboard'
    return sp.check_call(cmd, shell=True)


# Remove lines based on input 
def removeLines(lines, countOf1, countOf0, line, pos, sel):
    if sel == 0:
        bitCritOne = '0'
        bitCritTwo = '1'
    elif sel == 1:
        bitCritOne = '1'
        bitCritTwo = '0'

    if countOf1 > countOf0 and len(lines) > 1:
        if line[pos] == bitCritOne:
            lines.remove(line)
            if "v" in sys.argv:
                print(f"""
                    Removed line with 0 in position {pos}
                    COuntOf1 > CountOf0
                """)
    elif countOf0 > countOf1 and len(lines) > 1:
        if line[pos] == bitCritTwo:
            lines.remove(line)
            if "v" in sys.argv:
                print(f"""
                    Removed line with 1 in position {pos}
                    CountOf1 < CountOf0
                """)
    elif countOf1 == countOf0 and len(lines) > 1:
        if line[pos] == bitCritTwo:
            lines.remove(line)
            if "v" in sys.argv:
                print(f"""
                    Removed line with 1 in position {pos}
                    CountOf1 == CountOf0
                """)


def decodeInput(sel):
    lines = readInput()  # Get clean list of input
    for pos in range(12):
        countOf1 = 0
        countOf0 = 0
        # Count the amount of 1s and 0s in the lines bit at <pos>
        for line in lines:
            if line[pos] == '1':
                countOf1 += 1
            elif line[pos] == '0':
                countOf0 += 1
        print(f"""\n\n
            Amount of 1s in {pos}: {countOf1}
            Amount of 0s in {pos}: {countOf0}
        """)
        print(f"""
            List before: {lines}
        """)
        for line in lines:
            removeLines(lines, countOf1, countOf0, line, pos, sel)
    print(f"""
        Length of List: {len(lines)}
        List after: {lines}
        -------------------------------------------------------------------------------------------------------------------------
    """)
    result = lines[0]
    return result


# TODO: Add filtered values to array instead of removing them from the source one
# Finally print the result and copy it to the clipboard
oxyDec = int(decodeInput(0), 2)
co2Dec = int(decodeInput(1), 2)
result = oxyDec * co2Dec
print(f"""
    OxyDec: {oxyDec}
    Co2Dec: {co2Dec}
    Result: {result}
""")
copy2clip(result)
