import re

f = open("D:\Coding\Python-projects\leetcode\AdventofCode\calibrationinput.txt", "r")

numberSum = 0
numberString = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberHash = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def convertStringsToNumbers(line): #line is twonethreefour
    current_match = ""
    newLine = line

    for r in line:
        current_match += r #current match is "t"
        print("current match: ", current_match)
        match_found = False
        last_letter = ""
        for word in numberString: #goes through every word from one to nine
            if word.startswith(current_match): #if the word starts with the current_match
                match_found = True
                if current_match == word:
                    last_letter = current_match[-1]
                    newLine = re.sub(current_match, str(numberHash[word]) + last_letter, newLine, 1)
                    current_match = last_letter
            
        if match_found == False:
            current_match = r

    return newLine
    
def forwardFunction(line):

    fNum = 0

    for n in line:
        if n.isdigit():
            fNum += int(n)
            break
    
    return fNum

def backwardFunction(line):

    bNum = 0

    for n in line[::-1]:
        if n.isdigit():
            bNum += int(n)
            break
    
    return bNum

for line in f:

    #convert all strings to numbers, from left to right
    newLine = convertStringsToNumbers(line)

    #Find first number in line
    fNum = forwardFunction(newLine)
    
    #Find last number in line
    bNum = backwardFunction(newLine)

    num = (fNum * 10) + bNum
    numberSum = numberSum + num
    print("line: ", line, "newLine: ", newLine, "num: ", num, "numberSum:", numberSum)
# 55686