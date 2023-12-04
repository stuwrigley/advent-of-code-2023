#!/usr/bin/python3
import numpy as np

# part 1
with open('04_input.txt') as f:
    lines = [line.rstrip() for line in f]


def numMatchedNumbers(card):
    cardParts = card.split('|')
    winningNums = set(cardParts[0].split(':')[1].split())
    myNums = set(cardParts[1].split())
    matches = winningNums.intersection(myNums)
    return len(matches)


points = 0
for card in lines:
    numMatches = numMatchedNumbers(card)
    if numMatches == 1:
        points += 1
    if numMatches > 1:
        points += pow(2, numMatches - 1)

print("Part 1 answer:", points)

winnings = 0
cardCounts = np.ones(len(lines))
for cardID in range(len(lines)):
    numMatches = numMatchedNumbers(lines[cardID])
    numThisCard = int(cardCounts[cardID])
    winnings += numThisCard
    for cardOffset in range(1, min(numMatches + 1, len(lines) - 1)):
        cardCounts[cardID + cardOffset] += numThisCard

print("Part 2 answer:", winnings)
