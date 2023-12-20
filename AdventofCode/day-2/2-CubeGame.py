import json

f = open("D:\Coding\Python-projects\leetcode\AdventofCode\day-2\game.txt", "r")

first = "Game 1: 1 red, 3 blue, 11 green; 1 blue, 5 red; 3 blue, 5 green, 13 red; 6 red, 1 blue, 4 green; 16 red, 12 green"

results_list = []
gameSum = 0
redC = 12
greenC = 13
blueC = 14

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
    addToSum = True
    for list in dict['cubes']:
        if list.get('red', 0) > redC or list.get('green', 0) > greenC or list.get('blue', 0) > blueC:
            print("this list: ", list, " in game: ", dict['game'], "is a lie")
            addToSum = False
            break
    if addToSum == True:
        print('this game: ', dict['game'], 'is fine')
        gameSum += dict['game']
        print("gamesum added: ", gameSum)