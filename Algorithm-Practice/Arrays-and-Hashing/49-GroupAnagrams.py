import collections

def groupAnagrams(strs: list[str]) -> list:
    res = collections.defaultdict(list) #will return the list as a result if nothing else

    for s in strs: #for each str within the list of strings
        count = [0] * 26 #one for each letter of the alphabet

        for c in s: #for each letter in each str
            count[ord(c) - ord('a')] += 1 #will increase the count of the relevant letter of the alphabet by 1. ord(c) - ord('a') is done so that we can recalibrate ascii numbers to match our count.

        res[tuple(count)].append(s) #
    
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)
