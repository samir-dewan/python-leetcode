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
        # print("almanac['s']: ", almanac['s'], "l or e input: ", input, "l or e almanac['s'] + almanac['r'] - 1: ", almanac['r'] + almanac['s'] - 1)
        # print("destination number returned: ", almanac['d'] + input - almanac['s'], "from destination number: ", almanac["d"])
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
    snap = []
    crackle = []
    # wow=[]
    for i, seed in enumerate(seeds):
        pop.append(int(seed))
    for i, seed in enumerate(pop):
        if i % 2 == 0:
            snap.append(seed)
        else:
            crackle.append(seed)

    sections.pop(0)
    for i, section in enumerate(sections):
        results = []
        rows = pattern.findall(section)
        for row in rows:
            results.append({"d": int(row[0]), "s": int(row[1]), "r": int(row[2])})
        almanac.append(results)
    return pop, almanac, snap, crackle

seeds, almanacs, snap, crackle = sectionToObjects(f)
print("seeds: ", seeds)
print("snap: ", snap)
print("crackle: ", crackle)

testseed = 2149186375
locationList = []

def seedThroughAlmanacs(almanacs, seed):
    currentNum = seed
    for i, alm in enumerate(almanacs):
        nextStage = False
        for dsr in alm:
            currentNum, nextStage = converter(dsr, currentNum)
            if nextStage:
                break
    return currentNum

lowestLocation = 31599214
for i, s in enumerate(snap):
    print("trying out i: ", i, "with snap number: ", s)
    for j in range(0, crackle[i]):
        num = seedThroughAlmanacs(almanacs, s + j)
        if j % 1000000 == 0:
            print("number j: ", j, "with num: ", num)
        if num < lowestLocation:
            print("number: ", num, "is lower than lowestLocation: ", lowestLocation)
            lowestLocation = num

# def minAlmanac(almanacs):
#     for i, alm in enumerate(almanacs):
#         lowestNum = alm[0]
#         for dsr in alm:
#             if dsr['d'] < lowestNum['d']:
#                 lowestNum = dsr
#         print("lowest destination number in almanac: ", lowestNum)

# print(minAlmanac(almanacs))

# for seed in seeds:
#     locationList.append(seedThroughAlmanacs(almanacs, seed))

def minIdentifier(almanacs, d, snap, crackle):
    desired = d
    for i, alm in enumerate(reversed(almanacs)):
        #we have a desired number
        #we then go through every dsr in alm
        #if d <= desired number <= d + r
        #change the desired number to equal s
        for dsr in alm:
            if dsr['d'] <= desired <= dsr['d'] + dsr['r']:
                desired = dsr['s']
                print('desired number for alm: ', i + 1, 'is this: ', desired, 'in this: ', dsr)
                break

    for i, num in enumerate(snap):
        if num <= desired <= num + crackle[i]:
            print("lowest possible dest is found: ", d, "with: ", num, "and: ", crackle[i], "equals: ", num + crackle[i])
            print("You did it!")
            break
        else:
            print("doesn't work between: ", num, " and: ", num + crackle[i])

minIdentifier(almanacs, 0, snap, crackle)