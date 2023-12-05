#!/usr/bin/python3

with open('05_input.txt') as f:
    lines = [line.rstrip() for line in f]


def parseNumbers(numStr):
    return [int(i) for i in numStr.split()]


def findFromMap(map, src):
    for entry in map:
        if entry[1] <= src < (entry[1] + entry[2]):
            return entry[0] + src - entry[1]
    return src


# get the seeds
seeds = parseNumbers(lines[0].split(':')[1])

# parse and build the mappings
lineID = 3
maps = [[]]
mapID = 0
while lineID < len(lines):
    if lines[lineID] == '':
        lineID += 2
        maps.append([])
        mapID += 1
    maps[mapID].append(parseNumbers(lines[lineID]))
    lineID += 1

# part 1
location = float('inf')
for seed in seeds:
    loc = seed
    for map in maps:
        loc = findFromMap(map, loc)
    if loc < location:
        location = loc
print("Part 1 answer:", location)

# part 2

# need to deal with ranges intelligently rather than brute force trying every seed (billions)...
# make the ranges explicit in the maps (part 1 left the ranges as dest, src, extent)

seedRanges = [(src, src + ext) for src, ext in zip(seeds[::2], seeds[1::2])]
# print(seedRanges)

# parse and build the mappings
lineID = 3
maps = [[]]
mapID = 0
while lineID < len(lines):
    if lines[lineID] == '':
        lineID += 2
        maps.append([])
        mapID += 1
    [dest, src, extent] = parseNumbers(lines[lineID])
    maps[mapID].append([src, src + extent, dest - src])  # source range start, source range end, shift
    lineID += 1


# print(maps)


def expandMapAndAnalyse(rangeOfInterest, mapping):
    mapping = sorted(mapping, key=lambda span: span[0])  # sort sub-mappings in order

    mappingStart, mappingEnd = mapping[0][0], mapping[-1][1]
    actualStart, actualEnd = min(rangeOfInterest[0], mappingStart), max(rangeOfInterest[1], mappingEnd)

    # add the missing mappings at each extremity (since they're missing / undefined, they have a shift of 0)
    mapping = [(actualStart, mappingStart, 0)] + mapping + [(mappingEnd, actualEnd, 0)]

    # fill any missing gaps between the extremities (since they're missing / undefined, they have a shift of 0)
    missingMappings = [(end0, start1, 0) for (start0, end0, shift0), (start1, end1, shift1) in zip(mapping, mapping[1:])]
    mapping = mapping + missingMappings

    mapping = sorted(mapping, key=lambda span: span[0])  # sort sub-mappings in order

    # for each sub-mapping, find the overlap with the range of interest
    out = []
    for entryStart, entryEnd, entryShift in mapping:
        mappableStart, mappableEnd = max(rangeOfInterest[0], entryStart), min(rangeOfInterest[1], entryEnd)
        if mappableStart < mappableEnd:
            out.append((mappableStart + entryShift, mappableEnd + entryShift))
    return out


rangesOfInterest = seedRanges
for map in maps:
    refinedRanges = []
    for roi in rangesOfInterest:
        for nr in expandMapAndAnalyse(roi, map):
            refinedRanges.append(nr)
    rangesOfInterest = refinedRanges
rangesOfInterest = sorted(rangesOfInterest, key=lambda start: start[0])
print("Part 2 answer:", rangesOfInterest[0][0])
