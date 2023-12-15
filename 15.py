#!/usr/bin/python3

DAY = '15'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def getHASH(str):
    curVal = 0
    for char in str:
        curVal += ord(char)
        curVal *= 17
        curVal %= 256
    return curVal


def focusingPower(boxes):
    runningSum = 0
    for boxNum, box in boxes.items():
        for count, focalLength in enumerate(box[1]):
            runningSum += (boxNum + 1) * (count + 1) * focalLength
    return runningSum


# part 1
steps = lines[0].split(',')
runningSum = 0
for step in steps:
    runningSum += getHASH(step)
print("Part 1 answer:", runningSum)

# part 2
steps = lines[0].split(',')
boxes = {}
for step in steps:
    insertLens = '=' in step
    if insertLens:
        label, focalLen = step.split('=')
    else:
        label = step.split('-')[0]
    boxNum = getHASH(label)
    if boxNum not in boxes.keys():
        boxes[boxNum] = [[], []]
    if insertLens:
        if label not in boxes[boxNum][0]:
            boxes[boxNum][0].append(label)
            boxes[boxNum][1].append(int(focalLen))
        else:
            location = boxes[boxNum][0].index(label)
            boxes[boxNum][1][location] = int(focalLen)
    else:
        if label in boxes[boxNum][0]:
            location = boxes[boxNum][0].index(label)
            del boxes[boxNum][0][location]
            del boxes[boxNum][1][location]
        if not boxes[boxNum][0]:
            del boxes[boxNum]
print("Part 2 answer:", focusingPower(boxes))
