import re
f = open("D:\Coding\Python-projects\leetcode\AdventofCode\day-4\cards.txt", "r")
sumTotal = 0
scratchcards = []

def convertScratchTextToObject(text):
    scratches = []
    for row in text:
        scratch = {}
        r = re.sub("  ", " ", row)
        new_row = r.split(":")
        split_row = new_row[1].split("|")
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

def getLengthofWinningNumbers(scratchcard, scratchNum):
    winningNumbers = []
    for num in scratchcard["selected"]:
        if num in scratchcard["winning"]:
            winningNumbers.append(num)
    for i in range(scratchNum + 1, scratchNum + len(winningNumbers) + 1):
        scratchcards.append(i)

scratches = convertScratchTextToObject(f)

for i in range(len(scratches)):
    scratchcards.append(i + 1)

for scratchNum in scratchcards:
    getLengthofWinningNumbers(scratches[scratchNum - 1], scratchNum)
# for scratchNum in scratchcards:
#     for i, obj in enumerate(scratches):
#         winningNumbers = []
#         for num in obj["selected"]:
#             if num in obj["winning"]:
#                 # print("this number: ", num, "is a winner!: ", obj["winning"])
#                 winningNumbers.append(num)
#         for i in range(scratchNum, scratchNum + len(winningNumbers)):


#convert every scratchcard into their gameNumber: and then their selected: and winning:
#We have a list starting with card number 1
#We have a function that for each number within that list:
#Finds the card that matches that card number
#checks winningNumbers for that card
#appends a list of card numbers between the range of that card number and the length of winningNumbers
print(len(scratchcards))