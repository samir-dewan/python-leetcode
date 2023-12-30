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

def pushButton(t, winningD):
    wins = 0
    for i in range(1, int(t) + 1):
        distance = i * (int(t) - i)
        if distance > int(winningD):
            wins += 1
            print("i: ", i, "distance: ", distance, "is greater than winningD: ", winningD, ". wins are now: ", wins)
    return wins
    #distance = (time pushed)*(time left)

for i, t in enumerate(time):
    print("i: ", i, "t: ", t)
    winningWays.append(pushButton(t, distance[i]))

for num in winningWays:
    multiplied = multiplied * num

print("winning numbers: ", winningWays, "multiply to make: ", multiplied)