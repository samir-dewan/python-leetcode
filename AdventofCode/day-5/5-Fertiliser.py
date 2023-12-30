import re
f = open("D:\Coding\Python-projects\leetcode\AdventofCode\day-5\seeds.txt", "r")
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

def converter(almanac, input):
    if almanac['s'] <= input <= almanac['s'] + almanac['r'] - 1:
    #if almanac[1] <= seed <= almanac[1] + almanac[0]:
        #return (almanac[2] + almanac[1])
        print("almanac['s']: ", almanac['s'], "l or e input: ", input, "l or e almanac['s'] + almanac['r'] - 1: ", almanac['r'] + almanac['s'] - 1)
        print("destination number returned: ", almanac['d'] + input - almanac['s'], "from destination number: ", almanac["d"])
        return almanac['d'] + input - almanac['s'], True
    else:
        return input, False

#input is 50
#almanac is [r = 2, s = 49, d = 79]
#s+r-1 == input
#returns 79 + 50 - 49 = 80

def sectionToObjects(file):
    text = file.read()
    sections = re.split(r"\smap:\n", text)
    almanac = []
    pattern = re.compile(r'(\d+)\s+(\d+)\s+(\d+)\n')
    seedsNum = re.compile(r'(\d+)\s+')
    seeds = seedsNum.findall(sections[0]) #We have a list of seed numbers
    pop = []
    for seed in seeds:
        pop.append(int(seed))
    sections.pop(0)
    for i, section in enumerate(sections):
        results = []
        rows = pattern.findall(section)
        for row in rows:
            results.append({"d": int(row[0]), "s": int(row[1]), "r": int(row[2])})
        almanac.append(results)
    return pop, almanac

seeds, almanacs = sectionToObjects(f)
print("seeds: ", seeds)
print("almanacs: ", almanacs)

testseed = 2149186375
locationList = []

def seedThroughAlmanacs(almanacs, seed):
    currentNum = seed
    for i, alm in enumerate(almanacs):
        nextStage = False
        for dsr in alm:
            print("dsr: ", dsr, "in alm: ", i + 1)
            currentNum, nextStage = converter(dsr, currentNum)
            if nextStage:
                break
    print("currentNum is now: ", currentNum)
    return currentNum


for seed in seeds:
    locationList.append(seedThroughAlmanacs(almanacs, seed))
print(locationList)
print(min(locationList))
seedThroughAlmanacs(almanacs, min(locationList))