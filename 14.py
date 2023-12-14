#!/usr/bin/python3

DAY = '14'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def printPattern(pattern, offset=0):
    for line in pattern:
        print(' ' * offset + line)


def calculateLoad(pattern):
    load = 0
    numRows = len(pattern)
    for count, line in enumerate(pattern):
        load += line.count('O') * (numRows - count)
    return load


def tiltPlatformSmart(pattern, dir):
    rows = []
    if dir == NORTH or dir == SOUTH:  # we need to operate on the columns so make some temp strings from each col
        for colID in range(len(pattern[0])):
            rows.append([pattern[i][colID] for i in range(0, len(pattern))])
    else:
        rows = pattern

    tiltedStr = []
    for row in rows:
        betweenSquareRocks = ''.join(row).split('#')
        rowStr = ''
        for chunk in betweenSquareRocks:
            numRoundRocks = chunk.count('O')
            if dir == NORTH or dir == WEST:
                rowStr += 'O' * numRoundRocks + '.' * (len(chunk) - numRoundRocks) + '#'
            else:
                rowStr += '.' * (len(chunk) - numRoundRocks) + 'O' * numRoundRocks + '#'
        tiltedStr.append(rowStr[:-1])

    newPattern = []
    if dir == NORTH or dir == SOUTH:  # we need to convert these strings back to column elements
        for colID in range(len(pattern[0])):
            newPattern.append([tiltedStr[i][colID] for i in range(0, len(tiltedStr))])
    else:
        newPattern = tiltedStr
    return newPattern


def patternAsSingleStr(pattern):
    str = ''
    for line in pattern:
        str += line
    return str


def unfoldPattern(str, numRows):
    pattern = []
    numCols = int(len(str) / numRows)
    for row in range(numRows):
        pattern.append(str[(row * numCols):(row * numCols + numCols)])
    return pattern


# part 1
tiltedPlatform = tiltPlatformSmart(lines, NORTH)
print("Part 1 answer:", calculateLoad(tiltedPlatform))

# part 2
rotatedPattern = lines.copy()
previousPatterns = {}
numCycles = 1000000000
while numCycles > 0:
    key = patternAsSingleStr(rotatedPattern)
    if key in previousPatterns:
        numCycles %= (previousPatterns[key] - numCycles)
    previousPatterns[key] = numCycles
    for tiltDirection in [NORTH, WEST, SOUTH, EAST]:
        rotatedPattern = tiltPlatformSmart(rotatedPattern, tiltDirection)
    numCycles -= 1
print("Part 2 answer:", calculateLoad(rotatedPattern))
