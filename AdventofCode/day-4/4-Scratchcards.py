import re
f = open("D:\Coding\Python-projects\leetcode\AdventofCode\day-4\cards.txt", "r")
sumTotal = 0
def convertScratchTextToObject(text):
    scratches = []
    for row in text:
        scratch = {"winning": [], "selected": []}
        r = re.sub("  ", " ", row)
        new_row = r.split(":")
        new_row.pop(0)
        split_row = new_row[0].split("|")
        winning_row = split_row[0].strip().split(" ")
        scratch["winning"] = winning_row
        selected_row = split_row[1].strip().split(" ")
        scratch["selected"] = selected_row
        scratches.append(scratch)
    
    return scratches

def exponentiateNumbers(list):
    if len(list) == 0:
        return 0
    else:
        return 2 ** (len(list) - 1)
scratches = convertScratchTextToObject(f)
print(scratches)
for i, obj in enumerate(scratches):
    winningNumbers = []
    for num in obj["selected"]:
        if num in obj["winning"]:
            # print("this number: ", num, "is a winner!: ", obj["winning"])
            winningNumbers.append(num)
    sumTotal += exponentiateNumbers(winningNumbers)
    print("scratchcard: ", i, "had these as winners: ", winningNumbers, "which gave a total points of: ", exponentiateNumbers(winningNumbers))
print(sumTotal)