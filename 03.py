#!/usr/bin/python3
import re

# part 1
with open('03_input.txt') as f:
    lines = [line.rstrip() for line in f]


def isPartNum(numLine, numPos, numLen, maxLen, maxLines):
    for line in range(max(0, numLine - 1), min(numLine + 2, maxLines)):
        for pos in range(max(0, numPos - 1), min(maxLen, numPos + numLen + 1)):
            if not (lines[line][pos].isdigit()) and lines[line][pos] != '.':
                return True
    return False


partNumSum = 0
for lineID in range(len(lines)):
    possibleNums = re.findall(r'\d+|\D+', lines[lineID])
    numPosition = 0
    for num in possibleNums:
        numLen = len(num)
        if num.isdigit():
            if isPartNum(lineID, numPosition, numLen, len(lines[lineID]), len(lines)):
                partNumSum += int(num)
        numPosition += numLen

print("Part 1 answer:", partNumSum)

# part 2
with open('03_input.txt') as f:
    lines = [line.rstrip() for line in f]


def findPossibleGearPositions(line):
    return [i for i, ltr in enumerate(line) if ltr == '*']


def gearPower(lineID, pos, maxLines):  # adjacent to exactly two part numbers. returns 0 if not a gear
    adjacentNums = []

    for line in range(max(0, lineID - 1), min(lineID + 2, maxLines)):
        possibleNums = re.findall(r'\d+|\D+', lines[line])
        numPosition = 0
        for num in possibleNums:
            numLen = len(num)
            if num.isdigit():
                numPosRange = range(numPosition - 1, numPosition + numLen + 1)
                if pos in numPosRange:
                    adjacentNums.append(int(num))
            numPosition += numLen

    if len(adjacentNums) == 2:
        return adjacentNums[0] * adjacentNums[1]
    else:
        return 0


gearRatioSum = 0
for lineID in range(len(lines)):
    possibleGearPositions = findPossibleGearPositions(lines[lineID])
    for possibleGearPos in possibleGearPositions:
        gearRatioSum += gearPower(lineID, possibleGearPos, len(lines))
print("Part 2 answer:", gearRatioSum)
