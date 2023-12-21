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
    print("numcoords: ", numcoords)
    return numcoords

def convertChartoCoords(span, index):
    charcoords = (span[0], index)
    print("charcoords: ", charcoords)
    return charcoords

def checkNumHasNearbyCoord(numcoords, charcoords):
    for numcoord in numcoords:
        for coord in charcoords:
            distance = math.sqrt((numcoord[0] - coord[0]) ** 2 + (numcoord[1] - coord[1]) ** 2)
            if distance <= math.sqrt(2):
                print("charcoords: ", coord, " is close to numcoord: ", numcoord)
                return True
    
    return False

for index, row in enumerate(f):
    print("index: ", index)
    y = re.finditer("[0-9][0-9][0-9]|[0-9][0-9]|[0-9]", row)
    z = re.finditer("[^\d.\s]", row)
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

for obj in num_coords:
    checkCoords = checkNumHasNearbyCoord(obj["coords"], char_coords)
    if checkCoords == True:
        print("so this number has been added: ", obj["number"])
        totalSum += obj["number"]

print(totalSum)
