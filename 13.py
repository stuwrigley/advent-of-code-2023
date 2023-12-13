#!/usr/bin/python3

DAY = '13'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

patternBreaks = []
for i, line in enumerate(lines):
    if line == '':
        patternBreaks.append(i)
patternBreaks.append(len(lines))


def findHorizontalMirrorPoint(pattern):
    mirrorPoints = []
    for i in range(0, len(pattern) - 1):
        if pattern[i] == pattern[i + 1] and verifyHMP(pattern, i):
            mirrorPoints.append(i)
    return mirrorPoints


def findVerticalMirrorPoint(pattern):
    mirrorPoints = []
    for colID in range(0, len(pattern[0]) - 1):
        col1 = [pattern[i][colID] for i in range(0, len(pattern))]
        col2 = [pattern[i][colID + 1] for i in range(0, len(pattern))]
        if col1 == col2 and verifyVMP(pattern, colID):
            mirrorPoints.append(colID)
    return mirrorPoints


def verifyHMP(pattern, pos):
    for offset in range(1, min(pos, len(pattern) - pos - 2) + 1, 1):
        if pattern[pos - offset] != pattern[pos + offset + 1]:
            return False
    return True


def verifyVMP(pattern, pos):
    for offset in range(1, min(pos, len(pattern[0]) - pos - 2) + 1, 1):
        col1 = [pattern[i][pos - offset] for i in range(0, len(pattern))]
        col2 = [pattern[i][pos + offset + 1] for i in range(0, len(pattern))]
        if col1 != col2:
            return False
    return True


def printPattern(pattern, offset):
    for line in pattern:
        print('' * offset + line)


# for each pattern
part1score = 0
part2score = 0
patternStart = 0
for patternCount, patternBreak in enumerate(patternBreaks):
    pattern = []
    for i in range(patternStart, patternBreak):
        pattern.append(lines[i])
    patternStart = patternBreak + 1

    # part 1
    horMirrorPoints = findHorizontalMirrorPoint(pattern)
    verMirrorPoints = findVerticalMirrorPoint(pattern)

    for hmp in horMirrorPoints:
        part1score += (hmp + 1) * 100
    for vmp in verMirrorPoints:
        part1score += vmp + 1

    # part 2
    # alter each position in turn
    potentialHMPs = set()
    potentialVMPs = set()
    for row in range(len(pattern)):
        for col in range(len(pattern[0])):
            newPattern = pattern.copy()
            newChar = '.'
            if newPattern[row][col] == '.':
                newChar = '#'
            newPattern[row] = newPattern[row][:col] + newChar + newPattern[row][col + 1:]

            newHMP = findHorizontalMirrorPoint(newPattern)
            newVMP = findVerticalMirrorPoint(newPattern)

            for nhmp in newHMP:
                if nhmp not in horMirrorPoints:
                    potentialHMPs.add(nhmp)
            for vhmp in newVMP:
                if vhmp not in verMirrorPoints:
                    potentialVMPs.add(vhmp)

    for hmp in potentialHMPs:
        part2score += (hmp + 1) * 100
    for vmp in potentialVMPs:
        part2score += vmp + 1

print("Part 1 answer:", part1score)

# part 2
print("Part 2 answer:", part2score)
