#!/usr/bin/python3

DAY = '12'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def countPatterns(springs, groups, pos, currentGroupUnitsLeft, nextGroupIndex):
    key = (pos, currentGroupUnitsLeft, nextGroupIndex)
    if key in cache:
        return cache[key]
    if pos == len(springs):
        return currentGroupUnitsLeft <= 0 and nextGroupIndex == len(groups)  # have we got to the end of the pattern and used all possible hashes?

    count = 0
    if springs[pos] == '?' or springs[pos] == '.': 
        if currentGroupUnitsLeft <= 0:
            count += countPatterns(springs, groups, pos + 1, -1, nextGroupIndex)

    if springs[pos] == '?' or springs[pos] == '#':
        if currentGroupUnitsLeft > 0:
            count += countPatterns(springs, groups, pos + 1, currentGroupUnitsLeft - 1, nextGroupIndex)
        elif currentGroupUnitsLeft < 0 and nextGroupIndex < len(groups):
            count += countPatterns(springs, groups, pos + 1, groups[nextGroupIndex] - 1, nextGroupIndex + 1)

    cache[key] = count
    return count


cache = {}  # cache is only needed for part 2

# part 1
numArrangements = 0
for row in lines:
    springs, groups = row.split()
    groups = [int(i) for i in groups.split(',')]
    cache.clear()
    numArrangements += countPatterns(springs, groups, 0, -1, 0)
print("Part 1 answer:", numArrangements)

# part 2
numArrangements = 0
for row in lines:
    springs, groups = row.split()
    springs = ''.join([springs + '?'] * 5)[:-1]
    groups = [int(i) for i in groups.split(',')] * 5
    cache.clear()
    numArrangements += countPatterns(springs, groups, 0, -1, 0)
print("Part 2 answer:", numArrangements)
