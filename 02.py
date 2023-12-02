#!/usr/bin/python3

# part 1
with open('02_input.txt') as f:
    lines = [line.rstrip() for line in f]

maxCubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

validGameIDSum = 0
for line in lines:
    gamePossible = True
    lineParts = line.split(":")
    gameID = int(lineParts[0].split()[1])
    grabs = lineParts[1].split(";")
    for grab in grabs:
        cubes = grab.split(",")
        for cube in cubes:
            cubeCount = cube.split()
            if int(cubeCount[0]) > maxCubes[cubeCount[1]]:
                gamePossible = False
    if gamePossible:
        validGameIDSum += gameID

print("Part 1 answer:", validGameIDSum)

# part 2
with open('02_input.txt') as f:
    lines = [line.rstrip() for line in f]


def cubePower(cubeCounts):
    return cubeCounts["red"] * cubeCounts["blue"] * cubeCounts["green"]


powerSum = 0
for line in lines:
    lineParts = line.split(":")
    gameID = int(lineParts[0].split()[1])
    maxCubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    grabs = lineParts[1].split(";")
    for grab in grabs:
        cubes = grab.split(",")
        for cube in cubes:
            cubeCount = cube.split()
            cubeColour = cubeCount[1]
            cubeCount = int(cubeCount[0])
            if maxCubes[cubeColour] < cubeCount:
                maxCubes[cubeColour] = cubeCount
    powerSum += cubePower(maxCubes)

print("Part 2 answer:", powerSum)
