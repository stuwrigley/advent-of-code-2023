#!/usr/bin/python3

DAY = '19'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

firstWorkflow = 'in'
workflows = {}
parts = []
processingRules = True
for line in lines:
    if line == '':
        processingRules = False
        continue
    if processingRules:
        workflowName = line[:line.find('{')]
        rules = [r.split(':') for r in line[line.find('{') + 1:-1].split(',')]
        workflows[workflowName] = rules
    else:
        ratings = [int(r.split('=')[1]) for r in line[1:-1].split(',')]
        parts.append(ratings)

# part 1
total = 0
for part in parts:
    x, m, a, s = part
    nextWorkflow = firstWorkflow
    processNextPart = False
    while not processNextPart:
        for ruleID, rule in enumerate(workflows[nextWorkflow]):
            if ruleID == len(workflows[nextWorkflow]) - 1 or eval(rule[0]):
                if rule[-1] == 'A':
                    total += x + m + a + s
                    processNextPart = True
                elif rule[-1] == 'R':
                    processNextPart = True
                else:
                    nextWorkflow = rule[-1]
                break

print("Part 1 answer:", total)


def numRangeCombinations(partRanges):
    mult = 1
    for rangeMin, rangeMax in partRanges.values():
        mult *= (rangeMax - rangeMin + 1)
    return mult


def exploreRanges(partRanges, ruleName):
    answer = 0
    for rule in workflows[ruleName][:-1]:  # the last "rule" isn't a rule - it's the default - so don't process it as a rule
        part = rule[0][0]
        partRangeMin = partRanges[part][0]
        partRangeMax = partRanges[part][1]
        operator = rule[0][1]
        val = int(rule[0][2:])
        target = rule[1]
        if operator == '<':
            newRangeMin, newRangeMax = min(partRangeMin, val - 1), min(partRangeMax, val - 1)
        else:
            newRangeMin, newRangeMax = max(partRangeMin, val + 1), max(partRangeMax, val + 1)

        if newRangeMin <= newRangeMax:
            new_part = {**partRanges, part: (newRangeMin, newRangeMax)}
            if target == 'A':
                answer += numRangeCombinations(new_part)
            elif target != 'R':
                answer += exploreRanges(new_part, target)

        if operator == '<':
            newRangeMin, newRangeMax = max(partRangeMin, val), max(partRangeMax, val)
        else:
            newRangeMin, newRangeMax = min(partRangeMin, val), min(partRangeMax, val)

        partRanges = {**partRanges, part: (newRangeMin, newRangeMax)}
        if newRangeMin > newRangeMax:
            return answer

    defaultRule = workflows[ruleName][-1][0]
    if defaultRule == 'A':
        answer += numRangeCombinations(partRanges)
    elif defaultRule != 'R':
        answer += exploreRanges(partRanges, defaultRule)
    return answer


# part 2
partRanges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
print("Part 2 answer:", exploreRanges(partRanges, firstWorkflow))
