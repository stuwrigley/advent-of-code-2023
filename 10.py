#!/usr/bin/python3

DAY = '10'
TEST = False
inputFilename = DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

offsets = {"|": {(1, 0): (1, 0), (-1, 0): (-1, 0)},  # | is a vertical pipe connecting north and south.
           "-": {(0, 1): (0, 1), (0, -1): (0, -1)},  # - is a horizontal pipe connecting east and west.
           "L": {(1, 0): (0, 1), (0, -1): (-1, 0)},  # L is a 90-degree bend connecting north and east.
           "J": {(1, 0): (0, -1), (0, 1): (-1, 0)},  # J is a 90-degree bend connecting north and west.
           "7": {(0, 1): (1, 0), (-1, 0): (0, -1)},  # 7 is a 90-degree bend connecting south and west.
           "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},  # F is a 90-degree bend connecting south and east.
           }


def findStart():
    for xPos in range(len(lines)):
        for yPos in range(len(lines[0])):
            if lines[xPos][yPos] == 'S':
                return (xPos, yPos)


S = findStart()
dirOfTravel = (0, 1)

# part 1
visited = set()
visited.add(S)
curPos = (S[0] + dirOfTravel[0], S[1] + dirOfTravel[1])
visited.add(curPos)
curPipe = lines[curPos[0]][curPos[1]]
numSteps = 1
while curPipe != 'S':
    offset = offsets[curPipe][dirOfTravel]
    curPos = (curPos[0] + offset[0], curPos[1] + offset[1])
    visited.add(curPos)
    curPipe = lines[curPos[0]][curPos[1]]
    dirOfTravel = offset
    numSteps += 1
print("Part 1 answer:", int(numSteps / 2))

# part 2
area = 0
for xPos in range(len(lines)):
    isInside = False
    for yPos in range(len(lines[0])):
        curPos = (xPos, yPos)
        curPipe = lines[xPos][yPos]
        if curPos in visited and (curPipe == '|' or curPipe == '7' or curPipe == 'F'):
            isInside = not isInside
        if curPos not in visited and isInside:
            area += 1
print("Part 2 answer:", area)
