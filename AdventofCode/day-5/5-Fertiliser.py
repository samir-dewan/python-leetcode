import re
# f = open("D:\Coding\Python-projects\leetcode\AdventofCode\day-5\almanac.txt", "r")
f = open("D:\Coding\Python-projects\leetcode\AdventofCode\day-5\almanac.txt", "r")
#seed
#24

#seed-to-soil map
#We need to move this seed
#50 98 2
#52 50 48

#First number is destination range
#Second number is source range
#Third number is range length

#For first set of numbers 50, 98, 2, we know that
#the source range is [98, 99]
#the destination range is [50, 51]

#source range converts to destination in pairs so 98 turns to 50 and 99 turns to 51
#each list is therefore [d, s, r] and returns [[d, d+1, ...d+r-1], [s, s+1, ...s+r-1]]
#if s2 <= s1 <= s2+r return (d + s1 - s2)

#source is 50
#seed is 55
#dest is 90
#range is 6

#seed is in range of 50 + (6 - 1)
#will return destination of 90 + (6 - 1)

almanac = {}

seeds = []
seedToSoil = []
soilToFertiliser = []
fertiliserToWater = []
waterToLight = []
lightToTemp = []
tempToHumidity = []
humidityToLocation = []

def sourceChecker(almanac, input):
    if almanac['s'] <= input <= almanac['s'] + almanac['r'] - 1:
    #if almanac[1] <= seed <= almanac[1] + almanac[0]:
        #return (almanac[2] + almanac[1])
        return almanac['d'] + input - almanac['s']

#input is 50
#almanac is [r = 2, s = 49, d = 79]
#s+r-1 == input
#returns 79 + 50 - 49 = 80
    
def lineToObject(line):
    coords = re.split("/s", line)
    return {'d': coords[0], 's': coords[1], 'r': coords[2]}

def sectionToObjects(section):
    sections = re.split(":", section)
    return sections

sectionToObjects(f)