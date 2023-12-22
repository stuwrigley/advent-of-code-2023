#!/usr/bin/python3
from collections import deque

DAY = '21'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

ROCK = '#'

# part 1

# find start
start = (0, 0)
for row, line in enumerate(lines):
    if 'S' in line:
        start = (row, line.find('S'))

possibleGardens = set()
visited = set()
visited.add(start)
toCheck = deque()
toCheck.append((start, 64))

while toCheck:
    position, numStepsLeft = toCheck.popleft()
    if numStepsLeft % 2 == 0:
        possibleGardens.add(position)
    if numStepsLeft > 0:
        for offset in [UP, DOWN, LEFT, RIGHT]:
            nextPos = (position[0] + offset[0], position[1] + offset[1])
            if 0 <= nextPos[0] < len(lines) and 0 <= nextPos[1] < len(lines[0]) and lines[nextPos[0]][nextPos[1]] != ROCK and nextPos not in visited:
                visited.add(nextPos)
                toCheck.append((nextPos, numStepsLeft - 1))

print("Part 1 answer:", len(possibleGardens))

# part 2
possibleGardens = set()
visited = set()
visited.add(start)
toCheck = deque()
toCheck.append((start, 26501365))  # 26501365

while toCheck:
    position, numStepsLeft = toCheck.popleft()
    if numStepsLeft % 2 == 0:
        possibleGardens.add(position)
    if numStepsLeft > 0:
        for offset in [UP, DOWN, LEFT, RIGHT]:
            nextPos = (position[0] + offset[0], position[1] + offset[1])
            correctedPos = (nextPos[0] % len(lines), nextPos[1] % len(lines[0]))
            if lines[correctedPos[0]][correctedPos[1]] != ROCK and nextPos not in visited:
                visited.add(nextPos)
                toCheck.append((nextPos, numStepsLeft - 1))
print("Part 2 answer:", len(possibleGardens))
