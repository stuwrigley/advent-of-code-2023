#!/usr/bin/python3
DAY = '06'
TEST = False
inputFilename = DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]


def distanceTravelled(buttonPressTime, raceDuration):
    return buttonPressTime * (raceDuration - buttonPressTime)


# part 1
times = [int(i) for i in lines[0].split(":")[1].split()]
distances = [int(i) for i in lines[1].split(":")[1].split()]

multipliedWaysToWin = 1
for race in range(len(times)):
    waysToWin = 0
    for buttonTime in range(times[race] + 1):
        if distanceTravelled(buttonTime, times[race]) > distances[race]:
            waysToWin += 1
    multipliedWaysToWin *= waysToWin

print("Part 1 answer:", multipliedWaysToWin)

# part 2
time = int(''.join(lines[0].split(":")[1].split()))
dist = int(''.join(lines[1].split(":")[1].split()))

waysToWin = 0
for buttonTime in range(time + 1):
    if distanceTravelled(buttonTime, time) > dist:
        waysToWin += 1

print("Part 2 answer:", waysToWin)
