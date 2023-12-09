#!/usr/bin/python3
import numpy as np

DAY = '09'
TEST = False
inputFilename = DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def nextInSequence(seq):
    diffs = seq
    offset = 0
    while len(set(diffs)) > 1:
        diffs = np.diff(diffs)
        offset += diffs[-1]
    return seq + [seq[-1] + offset]


# part 1 & 2
runningSumPart1 = runningSumPart2 = 0
for line in lines:
    sequence = [int(i) for i in line.split()]
    runningSumPart1 += nextInSequence(sequence)[-1]
    runningSumPart2 += nextInSequence(sequence[::-1])[-1]

print("Part 1 answer:", runningSumPart1)
print("Part 2 answer:", runningSumPart2)
