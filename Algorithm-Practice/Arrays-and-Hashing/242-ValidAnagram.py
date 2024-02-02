#Create a function that returns true if two input strings are an anagram of one another, e.g. "abc" and "cba" returns True

def ValidAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): #if the lengths are different they can't be anagrams
        return False
    
    countS, countT = set(), set() #creates two dictionaries

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0) #the letter is a key, and the count becomes 1 + if the key doesn't exist, 0, else 1
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c, 0): #if there isn't an equivalent count of each letter in the first word, return false
            return False
    
    return True