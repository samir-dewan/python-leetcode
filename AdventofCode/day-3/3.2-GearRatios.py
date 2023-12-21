import re
import math

f = open("D:\Coding\Python-projects\leetcode\AdventofCode\day-3\parts.txt", "r")
char_coords = [] #list of tuples
num_coords = [] #{coords: tuple, num: integer}
totalSum = 0

def convertNumtoCoords(num, span, index):
    numcoords = {"number": int(num), "coords": []}
    for i in range(span[0], span[1]):
        numcoords["coords"].append((i, index))
    return numcoords

def convertChartoCoords(span, index):
    charcoords = (span[0], index)
    return charcoords

def checkCharHasNumNearby(charcoord, numcoords_array):
    adjacentCount = 0
    adjacentNumbers = []
    for numcoords in numcoords_array:
            for numcoord in numcoords["coords"]:
                distance = math.sqrt((charcoord[0] - numcoord[0]) ** 2 + (charcoord[1] - numcoord[1]) ** 2)
                if distance <= math.sqrt(2):
                    adjacentCount += 1
                    adjacentNumbers.append(numcoords["number"])
                    break
    
    if adjacentCount > 1:
        return adjacentNumbers[0] * adjacentNumbers[1]

    return 0


#for every coordinate in numcoords
#check if any of them are close to the charcoord
#if they are increase the adjacentCount by one, add the numcoord[number] to an array and continue onto the next numcoord
#if the adjacentCount > 1
#multiply the numbers in the array together
#return that result
#else return nothing

for index, row in enumerate(f):
    y = re.finditer("[0-9][0-9][0-9]|[0-9][0-9]|[0-9]", row)
    z = re.finditer("[*]", row)
    for o in y:
        numcoords = convertNumtoCoords(o.group(), o.span(), index)
        num_coords.append(numcoords)
    for j in z:
        charcoords = convertChartoCoords(j.span(), index)
        char_coords.append(charcoords)

for obj in char_coords:
    gearRatio = checkCharHasNumNearby(obj, num_coords)
    totalSum += gearRatio

print(totalSum)