#!/usr/bin/python3
import math

DAY = '18'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

offsets = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}


def printPattern(pattern, offset=0):
    for line in pattern:
        print(' ' * offset + line)


def mapArea(map):
    area = 0
    for row in map:
        area += row.count('#')
    return area


def buildMap(holes):
    minX = math.inf
    maxX = -math.inf
    minY = math.inf
    maxY = -math.inf
    for hole in holes:
        minX = min(hole[1], minX)
        maxX = max(hole[1], maxX)
        minY = min(hole[0], minY)
        maxY = max(hole[0], maxY)
    numRows = maxY - minY + 1
    numCols = maxX - minX + 1
    xOffset = abs(minX)
    yOffset = abs(minY)
    map = []
    for row in range(numRows):
        map.append('.' * numCols)
        for hole in holes:
            if hole[0] + yOffset == row:
                map[-1] = map[-1][:hole[1] + xOffset] + '#' + map[-1][hole[1] + xOffset + 1:]
    return map


def fillMap(map, startPos=(0, 0)):
    startRow = startPos[0]
    startCol = startPos[1]
    filledMap = map.copy()
    blocksToExplore = set()
    blocksToExplore.add((startRow, startCol))
    while blocksToExplore:
        currentBlock = blocksToExplore.pop()
        filledMap[currentBlock[0]] = filledMap[currentBlock[0]][:currentBlock[1]] + '#' + filledMap[currentBlock[0]][currentBlock[1] + 1:]
        for direction in offsets:
            neighbourRow = currentBlock[0] + offsets[direction][0]
            neighbourCol = currentBlock[1] + offsets[direction][1]
            if filledMap[neighbourRow][neighbourCol] == '.':
                blocksToExplore.add((neighbourRow, neighbourCol))
    return filledMap


# part 1
pos = [0, 0]
holes = []
for line in lines:
    dir, numBlocks, col = line.split()
    for step in range(int(numBlocks)):
        pos[0] += offsets[dir][0]
        pos[1] += offsets[dir][1]
        holes.append(pos.copy())
map = buildMap(holes)

startRow = 1
startCol = 0
for count, char in enumerate(map[1]):
    if char == '#':
        startCol = count + 1
        break
filledMap = fillMap(map, (startRow, startCol))
print("Part 1 answer:", mapArea(filledMap))

# part 2
dirs = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
trenchEnd = (0, 0)
trenches = set()
for line in lines:
    dir, numBlocks, col = line.split()
    numBlocks = int(col[2:7], 16)
    dir = dirs[int(col[-2])]
    trenchStart = trenchEnd
    trenchEnd = ((trenchStart[0] + offsets[dir][0] * numBlocks, trenchStart[1] + offsets[dir][1] * numBlocks))
    trenches.add((trenchStart, trenchEnd))

area = 0
trenchLength = 0
for trench in trenches:
    area += (trench[1][0] - trench[0][0]) * trench[0][1]  # simplification of the Gauss area formula
    trenchLength += max(abs(trench[0][0] - trench[1][0]), abs(trench[0][1] - trench[1][1]))
area = area + int(trenchLength / 2) + 1
print("Part 2 answer:", area)
