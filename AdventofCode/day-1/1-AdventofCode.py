f = open("D:\Coding\Python-projects\leetcode\AdventofCode\calibrationinput.txt", "r")

numberSum = 0

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

    #Find first number in line
    fNum = forwardFunction(line)
    
    #Find last number in line
    bNum = backwardFunction(line)

    num = (fNum * 10) + bNum
    numberSum = numberSum + num
    # print("line: ", line, "tens: ", fNum * 10, "units: ", bNum, "sum: ", numberSum)
