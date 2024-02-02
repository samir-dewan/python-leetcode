#Create a function that returns true if there is a duplicate within a list [a, b, c, d].

def containsDuplicate(list: list) -> bool:
    hashset = set() #Create the hashmap

    for n in list: #For every number in the list

        if n in hashset: #If the number is in the hashmap (it is a duplicate)
            return True #return true
        
        hashset.add(n) #Add the number to the hashset
    
    return False #It's gone through every number and there isn't a duplicate, so there isn't a duplicate

#print(containsDuplicate([1, 2, 3, 4, 3])) #test