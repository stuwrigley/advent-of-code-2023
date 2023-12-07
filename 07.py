#!/usr/bin/python3
import functools
from collections import Counter

DAY = '07'
TEST = False
DEBUG = True
inputFilename = DAY + '_input' + ('_test' if TEST else '') + '.txt'

with open(inputFilename) as f:
    lines = [line.rstrip().split() for line in f]


def scoreHand(hand, jokersActive):
    cardCounts = Counter(hand)
    counts = cardCounts.values()  # count each card
    if len(counts) == 1:  # Five of a kind
        return 7
    if max(counts) == 4:  # Four of a kind
        if jokersActive and 'J' in cardCounts.keys():
            return 7  # upgrade to five of a kind
        return 6
    if len(counts) == 2 and max(counts) == 3:  # Full house
        if jokersActive and 'J' in cardCounts.keys():
            return 7  # upgrade to five of a kind
        return 5
    if len(counts) == 3 and max(counts) == 3:  # Three of a kind
        if jokersActive and 'J' in cardCounts.keys():
            return 6  # upgrade to four of a kind
        return 4
    if len(counts) == 3 and max(counts) == 2:  # Two pair
        if jokersActive and cardCounts['J'] == 2:
            return 6  # upgrade to four of a kind
        if jokersActive and cardCounts['J'] == 1:
            return 5  # upgrade to full house
        return 3
    if len(counts) == 4:  # One pair
        if jokersActive and 'J' in cardCounts.keys():
            return 4  # upgrade to three of a kind
        return 2
    if len(counts) == 5:  # High card
        if jokersActive and cardCounts['J'] == 1:
            return 2  # upgrade to one pair
        return 1


def compare(hand1, hand2, cardScores, jokersActive):
    hand1Score = scoreHand(hand1[0], jokersActive)
    hand2Score = scoreHand(hand2[0], jokersActive)
    if hand1Score < hand2Score:
        return -1
    elif hand1Score > hand2Score:
        return 1
    else:  # hand is same type
        for cardID in range(len(hand1[0])):
            if cardScores[hand1[0][cardID]] < cardScores[hand2[0][cardID]]:
                return -1
            elif cardScores[hand1[0][cardID]] > cardScores[hand2[0][cardID]]:
                return 1


def compare1(hand1, hand2):
    cardScore = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return compare(hand1, hand2, cardScore, False)


def compare2(hand1, hand2):
    cardScore = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return compare(hand1, hand2, cardScore, True)


compareFunctions = [compare1, compare2]
for compareFnID in range(len(compareFunctions)):
    rankedHands = sorted(lines, key=functools.cmp_to_key(compareFunctions[compareFnID]))
    totalWinnings = 0
    count = 1
    for hand in rankedHands:
        totalWinnings += int(hand[1]) * count
        count += 1
    print("Part", compareFnID + 1, "answer:", totalWinnings)
