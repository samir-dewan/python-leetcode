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
                    print("charcoords: ", charcoord, " is close to numcoord: ", numcoord)
                    adjacentCount += 1
                    adjacentNumbers.append(numcoords["number"])
                    break
    
    if adjacentCount > 1:
        print('got it')
        print(adjacentNumbers)
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
    print("index: ", index)
    y = re.finditer("[0-9][0-9][0-9]|[0-9][0-9]|[0-9]", row)
    z = re.finditer("[*]", row)
    for o in y:
        numcoords = convertNumtoCoords(o.group(), o.span(), index)
        num_coords.append(numcoords)
    for j in z:
        charcoords = convertChartoCoords(j.span(), index)
        char_coords.append(charcoords)

print("num_coords: ", num_coords)
print("char_coords: ", char_coords)

#find every number within 
#finditer gives spans (place where item starts, item has ended by this point)
#therefore if we have an index of x and a span of (n, n+2) the number would be in position
#(x, n), (x, n+1)
#and the area we would need to search for a special character would be:
#(x-1, n-1) to (x+1, n+2)

for obj in char_coords:
    gearRatio = checkCharHasNumNearby(obj, num_coords)
    totalSum += gearRatio

print(totalSum)


#I have coordinates for all * signs
#and coordinates for all numbers
#for every * sign coordinate:
#check the list of numbers and find two numbers that are next to the sign coordinate