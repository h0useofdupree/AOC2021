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


# Copy result to clipboard
def copy2clip(txt):
    if type(txt) is not str:
        res = str(txt)
    else:
        res = txt
    cmd = 'echo ' + res.strip() + '| xclip -selection clipboard'
    return sp.check_call(cmd, shell=True)


# Remove lines based on input
def removeLines(countOf1, countOf0, line, pos, sel):
    if sel == 0:
        if countOf1 > countOf0 and len(lines) > 1:
            if line[pos] == '0':
                lines.remove(line)
                print(f"""
                    Removed line with 0 in position {pos}
                    COuntOf1 > CountOf0
                """)
        elif countOf1 < countOf0 and len(lines) > 1:
            if line[pos] == '1':
                lines.remove(line)
                print(f"""
                    Removed line with 1 in position {pos}
                    CountOf1 < CountOf0
                """)
        elif countOf1 == countOf0 and len(lines) > 1:
            if line[pos] == '1':
                lines.remove(line)
                print(f"""
                    Removed line with 1 in position {pos}
                    CountOf1 == CountOf0
                """)
    elif sel == 1:
        if countOf1 > countOf0 and len(lines) > 1:
            if line[pos] == '1':
                lines.remove(line)
                print(f"""
                    Removed line with 0 in position {pos}
                    COuntOf1 > CountOf0
                """)
        elif countOf1 < countOf0 and len(lines) > 1:
            if line[pos] == '0':
                lines.remove(line)
                print(f"""
                    Removed line with 1 in position {pos}
                    CountOf1 < CountOf0
                """)
        elif countOf1 == countOf0 and len(lines) > 1:
            if line[pos] == '0':
                lines.remove(line)
                print(f"""
                    Removed line with 1 in position {pos}
                    CountOf1 == CountOf0
                """)


def decodeInput(sel):
    for pos in range(12):
        countOf1 = 0
        countOf0 = 0
        for line in lines:  # Count the amount of 1s and 0s in the bit at <pos> for each line
            if line[pos] == '1':
                countOf1 += 1
            elif line[pos] == '0':
                countOf0 += 1

        print(f"""


            Amount of 1s in {pos}: {countOf1}
            Amount of 0s in {pos}: {countOf0}
        """)
        oxyLines = lines
        co2Lines = lines

        if sel == 0:
            print(f"""
                List before: {oxyLines}
                Starting to decode oxyLines
            """)
            for line in oxyLines:  # Remove the lines beginning with 1 or 0 when countOf1>countOf0 or countOf1<countOf0 respectively
                removeLines(countOf1, countOf0, line, pos, 0)
        elif sel == 1:
            print(f"""
                List before: {co2Lines}
                Starting to decode co2Lines
            """)
            for line in co2Lines:  # Remove the lines beginning with 1 or 0 when countOf1>countOf0 or countOf1<countOf0 respectively
                removeLines(countOf1, countOf0, line, pos, 1)
    print(f"""
        Length of List: {len(lines)}
        List after: {lines}
        _____________________________________________________________________
    """)
    result = lines[0]
    return result


# decodedInput = decodeInput()


# print(f"""
#     Gamma in decimal: {oxyDec}
#     Epsilon in deciaml: {co2Dec}
# """)

# # Finally print the result and copy it to the clipboard
oxyDec = int(decodeInput(0), 2)
co2Dec = int(decodeInput(1), 2)
result = oxyDec * co2Dec
print(f"""
    OxyDec: {oxyDec}
    Co2Dec: {co2Dec}
    Result: {result}
""")
copy2clip(result)
