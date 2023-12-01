#!/usr/bin/python3
import re

#part 1
with open('01_input.txt') as f:
    lines = [line.rstrip() for line in f]

total=0
for line in lines:
    numbers = re.findall(r'\d', line)
    total += int(str(numbers[0])+str(numbers[-1]))
print("Part 1 answer:",total)



#part 2
with open('01_input.txt') as f:
    lines = [line.rstrip() for line in f]

def convertToInt(strNum):
   numDict = {
     "one": 1,
     "two": 2,
     "three": 3,
     "four" : 4,
     "five": 5,
     "six": 6,
     "seven": 7,
     "eight": 8,
     "nine": 9
   }
   try:
      return(int(strNum))
   except ValueError:
      return numDict[strNum]

total=0
for line in lines:
    numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    curNum=int(str(convertToInt(convertToInt(numbers[0])))+str(convertToInt(convertToInt(numbers[-1]))))
    total += curNum
print("Part 2 answer:",total)
