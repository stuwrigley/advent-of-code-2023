#!/usr/bin/python3
import numpy

DAY = '08'
TEST = False
inputFilename = DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

turnInstructions = lines[0]
numTurnInstructions = len(turnInstructions)

directions = {}
for line in lines[2::]:
    parts = line.split()
    startNode = parts[0]
    if startNode not in directions:
        directions[startNode] = {}
    directions[startNode]['L'] = parts[2][1:-1]
    directions[startNode]['R'] = parts[3][:-1]

# part 1
currentNode = 'AAA'
turnCount = 0
while True:
    currentNode = directions[currentNode][turnInstructions[turnCount % numTurnInstructions]]
    turnCount += 1
    if currentNode == 'ZZZ':
        break
print("Part 1 answer:", turnCount)

# part 2
concurrentNodes = []
for node in directions.keys():
    if node[-1] == 'A':
        concurrentNodes.append(node)

turnCount = 0
times = {}
while True:
    for concurrentNodeID, node in enumerate(concurrentNodes):
        concurrentNodes[concurrentNodeID] = directions[node][turnInstructions[turnCount % numTurnInstructions]]
        if concurrentNodes[concurrentNodeID][-1] == 'Z':
            times[concurrentNodeID] = turnCount + 1
            if len(times) == len(concurrentNodes):
                print("Part 2 answer:", numpy.lcm.reduce(list(times.values())))
                exit()
    turnCount += 1
