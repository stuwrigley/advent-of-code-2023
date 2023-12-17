#!/usr/bin/python3
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
    stillToProcess = [(0, (0, 0), (0, 1), 0)]  # heatLoss, position, direction, stepsInThisDirection
    seen = set()
    while stillToProcess:
        heatLoss, (row, col), (rowDir, colDir), stepsInThisDirection = heapq.heappop(stillToProcess)

        if row == numRows - 1 and col == numCols - 1:
            if doPart1:
                return heatLoss
            elif stepsInThisDirection >= 4:
                return heatLoss

        if ((row, col), (rowDir, colDir), stepsInThisDirection) in seen:
            continue
        seen.add(((row, col), (rowDir, colDir), stepsInThisDirection))

        for count, newDir in enumerate(newDirections((rowDir, colDir))):
            if count == 0:
                newStepsInThisDirection = stepsInThisDirection + 1
            else:
                newStepsInThisDirection = 1

            if (doPart1 and newStepsInThisDirection <= 3) or (
                    not doPart1 and (stepsInThisDirection < 10 and count == 0) or (stepsInThisDirection >= 4 and count > 0)):
                nr = row + newDir[0]
                nc = col + newDir[1]
                if 0 <= nr < numRows and 0 <= nc < numCols:
                    heapq.heappush(stillToProcess, (heatLoss + int(lines[nr][nc]), (nr, nc), newDir, newStepsInThisDirection))


# part 1
print("Part 1 answer:", solve(True))

# part 2
print("Part 2 answer:", solve(False))
