import json

f = open("D:\Coding\Python-projects\leetcode\AdventofCode\day-2\game.txt", "r")

results_list = []
gameSum = 0

def convertGamesToDict(games):
    for game_str in games:
        cubesl = game_str.strip().split(": ")
        header = int(cubesl[0].split("Game ")[1])
        cube_info = cubesl[1].strip().split(";")
        cubes=[]

        for cube_str in cube_info:
            cube_single = cube_str.split(", ")
            cube={}
            for c in cube_single:
                count, colour = c.strip().split(" ")
                cube[colour] = int(count)
            cubes.append(cube)

        results_list.append({"game": header, "cubes": cubes})

    return results_list

dictList = convertGamesToDict(f)
for dict in dictList:
    redC = 1
    blueC = 1
    greenC = 1
    for list in dict['cubes']:
        if list.get('red', 0) > redC:
            redC = list['red']
        if list.get('green', 0) > greenC:
            greenC = list['green']
        if list.get('blue', 0) > blueC:
            blueC = list['blue']
    gameSum += blueC * greenC * redC
    print("with a red, blue, green min of: ", redC, blueC, greenC, "gameSum is: ", gameSum)