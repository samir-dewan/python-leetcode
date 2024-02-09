def ValidPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1 #initialises left and right pointers at start and end

    def isAlphanum(self, c: str) -> bool: #check char is alphanumeric
        return (ord('A') <= ord(c) <= ord('Z') or #if the letter is between A - Z ascii-wise
                ord('a') <= ord(c) <= ord('z') or #if the letter is between a - z ascii-wise
                ord('0') <= ord(c) <= ord('9')) #if the letter is between 0 - 9 ascii-wise

    while l < r: #make sure they don't cross over
        while l < r and not isAlphanum(s[l]): #if we haven't crossed over and the pointer is on a non-alphanumeric char
            l += 1
        
        while r > l and not isAlphanum(s[r]):
            r -= 1
        
        if s[l].lower() != s[r].lower():
            return False
        
    return True
