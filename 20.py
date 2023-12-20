#!/usr/bin/python3
import collections
import math

DAY = '20'
TEST = False
inputFilename = 'data/' + DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip() for line in f]

HIGH = 1
LOW = 2


class FlipFlop:

    def __init__(self, on=False):
        self.on = on

    def __str__(self):
        return f"FlipFlop: is on? {self.on}"

    def processInput(self, source, input):
        if input == LOW:
            self.on = not self.on
            if self.on:
                return HIGH
            else:
                return LOW


class Conjunction:
    def __init__(self):
        self.previousInputs = collections.defaultdict()

    def __str__(self):
        return f"Conjunction: history: {self.previousInputs}"

    def setConnectionsIn(self, cons):
        for con in cons:
            self.previousInputs[con] = LOW

    def processInput(self, source, input):
        self.previousInputs[source] = input
        if len(set(self.previousInputs.values())) == 1 and self.previousInputs[list(self.previousInputs.keys())[0]] == HIGH:
            return LOW
        else:
            return HIGH


# parse the input and build the graph
modules = collections.defaultdict()
firstTargets = collections.deque()
flipFlops = []
conjunctions = []
for line in lines:
    source, arrow, *targets = line.split()
    cleanTargets = []
    for target in targets:
        cleanTargets.append(target.split(',')[0])
    targets = cleanTargets
    if source == 'broadcaster':
        for target in targets:
            firstTargets.append([source, target, LOW])
    else:
        if source[0] == '%':
            flipFlops.append(source[1:])
            modules[source[1:]] = [FlipFlop(), targets]
        else:
            conjunctions.append(source[1:])
            modules[source[1:]] = [Conjunction(), targets]

# need to know each Conjunctions feeders to initialise their memories to LOW
for conjunction in conjunctions:
    inputsToThisConjunction = []
    for module in modules.items():
        if conjunction in module[1][1]:
            inputsToThisConjunction.append(module[0])
    modules[conjunction][0].setConnectionsIn(inputsToThisConjunction)

# this is for part 2
# the end node rx is fed by a single flipflop which is in turn fed by a bunch of other flipflops
# for rx to get a LOW, its feeding flipflop must get all HIGHs from its feeder flipflops
# so we need to find their names so we can note the button press number when they send a HIGH
# Lowest Common Multiplier of all these will give is the part 2 answer
rxFeeder = ''
for module in modules.items():
    if 'rx' in module[1][1]:
        rxFeeder = module[0]
rxFeederFeeders = []
for module in modules.items():
    if rxFeeder in module[1][1]:
        rxFeederFeeders.append(module[0])
rffCycles = collections.defaultdict()

lowPulseCount = 0
highPulseCount = 0
buttonPress = 0
while True:
    lowPulseCount += len(firstTargets) + 1  # the starting pulses plus the LOW from the button to the broadcaster
    modulesToProcess = firstTargets.copy()
    while modulesToProcess:
        source, targetModule, pulse = modulesToProcess.popleft()

        if source in rxFeederFeeders and pulse == HIGH:
            if source not in rffCycles:
                rffCycles[source] = buttonPress + 1
            if len(rffCycles) == len(rxFeederFeeders):
                print("Part 2 answer:", math.lcm(*list(rffCycles.values())))
                exit()

        if targetModule in modules.keys():  # some lead nowhere (like output and 'rx')
            newPulse = modules[targetModule][0].processInput(source, pulse)
            if newPulse is not None:  # a flipflop returns nothing in response to HIGH...
                for target in modules[targetModule][1]:
                    modulesToProcess.append([targetModule, target, newPulse])
                    if newPulse == HIGH:
                        highPulseCount += 1
                    else:
                        lowPulseCount += 1
    if buttonPress == 999:
        print("Part 1 answer:", lowPulseCount * highPulseCount)
    buttonPress += 1
