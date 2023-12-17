#!/usr/bin/python3
import math
import heapq

DAY = '17'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def newDirections(curDir):
    flippedDir = curDir[::-1]
    tuple(x * -1 for x in curDir)
    return [curDir, flippedDir, tuple(x * -1 for x in flippedDir)]


def solve(doPart1):
    numRows = len(lines)
    numCols = len(lines[0])
    stillToProcess = [(0, (0, 0), (0, 1), 0)]  # heatLoss, row, col, direction, stepsInThisDirection
    seen = {}
    while stillToProcess:
        heatLoss, pos, direction, stepsInThisDirection = heapq.heappop(stillToProcess)

        if (pos, direction, stepsInThisDirection) in seen:
            continue
        seen[(pos, direction, stepsInThisDirection)] = heatLoss

        for count, newDir in enumerate(newDirections(direction)):
            if doPart1 and count == 0 and stepsInThisDirection == 3:  # first new dir is always previous dir
                continue
            if not doPart1 and ((count > 0 and stepsInThisDirection < 4) or (count == 0 and stepsInThisDirection >= 10)):
                continue

            if count == 0:
                newStepsInThisDirection = stepsInThisDirection + 1
            else:
                newStepsInThisDirection = 1

            nextPos = (pos[0] + newDir[0], pos[1] + newDir[1])
            if 0 <= nextPos[0] < numRows and 0 <= nextPos[1] < numCols:
                heapq.heappush(stillToProcess, (heatLoss + int(lines[nextPos[0]][nextPos[1]]), nextPos, newDir, newStepsInThisDirection))

    smallestHeatLoss = math.inf
    for (pos, direction, stepsInThisDirection), heatLoss in seen.items():
        if pos[0] == numRows - 1 and pos[1] == numCols - 1:
            smallestHeatLoss = min(smallestHeatLoss, heatLoss)
    return smallestHeatLoss


# part 1
print("Part 1 answer:", solve(True))

# part 2
print("Part 2 answer:", solve(False))
