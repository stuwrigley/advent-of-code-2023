#!/usr/bin/python3

DAY = '16'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def moveTilePosition(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def withinGrid(pos):
    return pos[0] >= 0 and pos[0] < len(lines) and pos[1] >= 0 and pos[1] < len(lines[0])


def numEnergised(currentTile, directionOfTravel):
    energised = set()
    stepsToProcess = set()
    stepsToProcess.add((currentTile, directionOfTravel))
    alreadyProcessed = set()
    while stepsToProcess:
        step = stepsToProcess.pop()
        currentTile = step[0]
        directionOfTravel = step[1]
        energised.add(currentTile)

        tileChar = lines[currentTile[0]][currentTile[1]]
        nextDirs = []
        if tileChar == '.' or (tileChar == '-' and (directionOfTravel == LEFT or directionOfTravel == RIGHT)) or (
                tileChar == '|' and (directionOfTravel == UP or directionOfTravel == DOWN)):
            nextDirs = [directionOfTravel]
        elif tileChar == '-' and (directionOfTravel == UP or directionOfTravel == DOWN):
            nextDirs = [LEFT, RIGHT]
        elif tileChar == '|' and (directionOfTravel == LEFT or directionOfTravel == RIGHT):
            nextDirs = [UP, DOWN]
        elif (tileChar == '/' and directionOfTravel == RIGHT) or (tileChar == '\\' and directionOfTravel == LEFT):
            nextDirs = [UP]
        elif (tileChar == '/' and directionOfTravel == LEFT) or (tileChar == '\\' and directionOfTravel == RIGHT):
            nextDirs = [DOWN]
        elif (tileChar == '/' and directionOfTravel == UP) or (tileChar == '\\' and directionOfTravel == DOWN):
            nextDirs = [RIGHT]
        elif (tileChar == '/' and directionOfTravel == DOWN) or (tileChar == '\\' and directionOfTravel == UP):
            nextDirs = [LEFT]

        for changeInDir in nextDirs:
            nextTile = moveTilePosition(currentTile, changeInDir)
            if withinGrid(nextTile):
                nextToBeProcessed = (nextTile, changeInDir)
                if nextToBeProcessed not in alreadyProcessed:
                    alreadyProcessed.add(nextToBeProcessed)
                    stepsToProcess.add(nextToBeProcessed)
    return len(energised)


# part 1
currentTile = (0, 0)
directionOfTravel = RIGHT
print("Part 1 answer:", numEnergised(currentTile, directionOfTravel))

# part 2
biggestEnergised = 0
for colPos in range(len(lines[0])):
    curEnergised = numEnergised((0, colPos), DOWN)
    if curEnergised > biggestEnergised:
        biggestEnergised = curEnergised
    curEnergised = numEnergised((len(lines) - 1, colPos), UP)
    if curEnergised > biggestEnergised:
        biggestEnergised = curEnergised
for rowPos in range(len(lines)):
    curEnergised = numEnergised((rowPos, 0), RIGHT)
    if curEnergised > biggestEnergised:
        biggestEnergised = curEnergised
    curEnergised = numEnergised((rowPos, len(lines[0]) - 1), LEFT)
    if curEnergised > biggestEnergised:
        biggestEnergised = curEnergised
print("Part 2 answer:", biggestEnergised)
