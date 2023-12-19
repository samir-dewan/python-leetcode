class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #for every character r in string s
        #check if s[r] is unique
        #we have a pointer looking at the leftmost side (l) and another pointer looking at
        #the rightmost side (r)
        #if s[r] is unique with the range of l to r then carry on (increase the length of the
        #distance between l and r)
        #if s[r] is not unique, l needs to become smaller until s[r] is unique
        #we have a variable that checks the length of l to r.

        charset = set()
        l = 0
        res = 0

        for r in range(len(s)): #rightmost pointer
            while s[r] in charset: #while rightmost letter is in the window
                charset.remove(s[l]) #remove leftmost letter until we remove duplicate
                l += 1  #make window smaller
            charset.add(s[r]) #add rightmost letter to window
            res = max(res, r-l+1) #largest between the largest window we've seen and the current window
        return res
