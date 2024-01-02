import re

f = open(r"D:\Coding\Python-projects\leetcode\AdventofCode\day-7\hands.txt", "r")


def convertToObj(file):
    obj = []
    text = file.read()
    pattern = re.compile(r'(\w+)\s+(\d+)')
    lines = pattern.findall(text)
    for line in lines:
        obj.append({"hand": line[0], "bid": int(line[1])})
    return obj

allHands = convertToObj(f)

def handChecker(hand):
    five = re.compile(r'(.)\1\1\1\1')
    four = re.compile(r'.*(.).*\1.*\1.*\1')
    fh = re.compile(r'(.)(.)(\1|\2){3}')
    fh2 = re.compile(r'(.)\1(.)\2{2}')
    fh3 = re.compile(r'(.)\1\1(.)\2')
    three = re.compile(r'.*.*(.).*\1.*\1')
    twopair = re.compile(r'.*(.).*(.).*(\1|\2).*(\1|\2)')
    twopair2 = re.compile(r'.*(.)\1.*(.).*\2')
    twopair3 = re.compile(r'.*(.).*\1(.).*\2')
    two = re.compile(r'(.).*\1')
    if five.findall(hand['hand']):
        return 7
    if four.findall(hand['hand']):
        return 6
    if fh.findall(hand['hand']) or fh2.findall(hand['hand']) or fh3.findall(hand['hand']):        
        return 5
    if three.findall(hand['hand']):
        return 4
    if twopair.findall(hand['hand']) or twopair2.findall(hand['hand']) or twopair3.findall(hand['hand']):
        return 3
    if two.findall(hand['hand']):
        return 2
    return 1

FiveOfs = []
FourOfs = []
fhOfs = []
ThreeOfs = []
twoPairOfs = []
TwoOfs = []
OneOfs = []

finalList = []

for hand in allHands:
    Handcheck = handChecker(hand)
    if Handcheck == 7:
        FiveOfs.append(hand)
    if Handcheck == 6:
        FourOfs.append(hand)
    if Handcheck == 5:
        fhOfs.append(hand)
    if Handcheck == 4:
        ThreeOfs.append(hand)
    if Handcheck == 3:
        twoPairOfs.append(hand)
    if Handcheck == 2:
        TwoOfs.append(hand)
    if Handcheck == 1:
        OneOfs.append(hand)

print("FiveOfs: ", len(FiveOfs))
print("FourOfs: ", len(FourOfs))
print("FullHouses: ", len(fhOfs))
print("ThreeOfs: ", len(ThreeOfs))
print("TwoPairs: ", len(twoPairOfs))
print("TwoOfs: ", len(TwoOfs))
print("OneOfs: ", len(OneOfs))
print("total: ", len(FiveOfs) + len(FourOfs) + len(fhOfs) + len(ThreeOfs) + len(twoPairOfs) + len(TwoOfs) + len(OneOfs))

custom_order = 'AKQJT98765432'

sorted_fives = sorted(FiveOfs, key=lambda x: (custom_order.index(x['hand'][0]), custom_order.index(x['hand'][1]), custom_order.index(x['hand'][2]), custom_order.index(x['hand'][3]), custom_order.index(x['hand'][4])))
sorted_fours = sorted(FourOfs, key=lambda x: (custom_order.index(x['hand'][0]), custom_order.index(x['hand'][1]), custom_order.index(x['hand'][2]), custom_order.index(x['hand'][3]), custom_order.index(x['hand'][4])))
sorted_fhs = sorted(fhOfs, key=lambda x: (custom_order.index(x['hand'][0]), custom_order.index(x['hand'][1]), custom_order.index(x['hand'][2]), custom_order.index(x['hand'][3]), custom_order.index(x['hand'][4])))
sorted_threes = sorted(ThreeOfs, key=lambda x: (custom_order.index(x['hand'][0]), custom_order.index(x['hand'][1]), custom_order.index(x['hand'][2]), custom_order.index(x['hand'][3]), custom_order.index(x['hand'][4])))
sorted_twoPairs = sorted(twoPairOfs, key=lambda x: (custom_order.index(x['hand'][0]), custom_order.index(x['hand'][1]), custom_order.index(x['hand'][2]), custom_order.index(x['hand'][3]), custom_order.index(x['hand'][4])))
sorted_twos = sorted(TwoOfs, key=lambda x: (custom_order.index(x['hand'][0]), custom_order.index(x['hand'][1]), custom_order.index(x['hand'][2]), custom_order.index(x['hand'][3]), custom_order.index(x['hand'][4])))
sorted_ones = sorted(OneOfs, key=lambda x: (custom_order.index(x['hand'][0]), custom_order.index(x['hand'][1]), custom_order.index(x['hand'][2]), custom_order.index(x['hand'][3]), custom_order.index(x['hand'][4])))

#2q2tt in twos, not twopairs
print(sorted_twos)

def appendToMain(hands):
    for hand in hands:
        finalList.append(hand)

appendToMain(sorted_fives)
appendToMain(sorted_fours)
appendToMain(sorted_fhs)
appendToMain(sorted_threes)
appendToMain(sorted_twoPairs)
appendToMain(sorted_twos)
appendToMain(sorted_ones)

sum = 0
for i, hand in enumerate(finalList):
    sum += (hand['bid'] * (1000 - i))

print(sum)