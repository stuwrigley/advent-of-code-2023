#!/usr/bin/python3
import numpy as np

DAY = '11'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def expandUniverse(sky):
    emptyCols = np.where(~sky.any(axis=0))[0]
    addedSoFar = 0
    for col in emptyCols:
        sky = np.c_[sky[:, 0:col + addedSoFar], np.zeros(len(sky)), sky[:, col + addedSoFar:]]
        addedSoFar += 1
    emptyRows = np.where(~sky.any(axis=1))[0]
    addedSoFar = 0
    for row in emptyRows:
        sky = np.r_[sky[0:row + addedSoFar, :], np.zeros((1, len(sky[0]))), sky[row + addedSoFar:, :]]
        addedSoFar += 1
    return sky


# part 1
gridSize = len(lines)
sky = np.zeros((gridSize, gridSize))
for xPos in range(len(lines)):
    for yPos in range(len(lines[0])):
        if lines[xPos][yPos] == '#':
            sky[xPos][yPos] = 1

sky = expandUniverse(sky)
galaxyPositions = np.argwhere(sky == 1)
distanceSum = 0
for gal1 in range(0, len(galaxyPositions)):
    for gal2 in range(gal1 + 1, len(galaxyPositions)):
        dist = abs(galaxyPositions[gal2][0] - galaxyPositions[gal1][0]) + abs(galaxyPositions[gal2][1] - galaxyPositions[gal1][1])
        distanceSum += dist

print("Part 1 answer:", distanceSum)

# part 2
sky = np.zeros((gridSize, gridSize))
for xPos in range(len(lines)):
    for yPos in range(len(lines[0])):
        if lines[xPos][yPos] == '#':
            sky[xPos][yPos] = 1

emptyCols = np.where(~sky.any(axis=0))[0]
emptyRows = np.where(~sky.any(axis=1))[0]

galaxyPositions = np.argwhere(sky == 1)

distanceSum = 0
emptyRowColMultiplier = 1000000
for gal1 in range(0, len(galaxyPositions)):
    for gal2 in range(gal1 + 1, len(galaxyPositions)):
        dist = abs(galaxyPositions[gal2][0] - galaxyPositions[gal1][0]) + abs(galaxyPositions[gal2][1] - galaxyPositions[gal1][1])

        emptyRowsTraversed = len(np.where(np.logical_and(emptyRows >= min(galaxyPositions[gal1][0], galaxyPositions[gal2][0]),
                                                         emptyRows <= max(galaxyPositions[gal1][0], galaxyPositions[gal2][0])))[0])

        emptyColsTraversed = len(np.where(np.logical_and(emptyCols >= min(galaxyPositions[gal1][1], galaxyPositions[gal2][1]),
                                                         emptyCols <= max(galaxyPositions[gal1][1], galaxyPositions[gal2][1])))[0])

        distanceSum += dist + emptyRowColMultiplier * emptyRowsTraversed + emptyRowColMultiplier * emptyColsTraversed - (
                    emptyRowsTraversed + emptyColsTraversed)

print("Part 2 answer:", distanceSum)
