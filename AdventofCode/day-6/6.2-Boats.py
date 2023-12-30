import re

f = open("D:\Coding\Python-projects\leetcode\AdventofCode\day-6\ships.txt", "r")

winningWays = []
multiplied = 1

def convertToList(file):
    text = file.read()
    pattern = re.compile(r'(\d+)\s+(\d+)\s+(\d+)\s+(\d+)')
    lines = pattern.findall(text)
    time = lines[0]
    distance = lines[1]
    return time, distance

time, distance = convertToList(f)
print("times: ", time)
print("distance: ", distance)

bigTime = ''.join(map(str, time))
print("bigTime: ", bigTime)

bigDist = ''.join(map(str, distance))
print("bigDist: ", bigDist)

def pushButton(t, winningD):
    wins = 0
    for i in range(1, int(t) + 1):
        distance = i * (int(t) - i)
        if distance > int(winningD):
            wins += 1
    return wins
    #distance = (time pushed)*(time left)

allWins = pushButton(bigTime, bigDist)

print("winning numbers: ", allWins)

