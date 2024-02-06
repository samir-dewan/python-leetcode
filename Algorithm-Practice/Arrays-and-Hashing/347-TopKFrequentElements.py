def TopKFrequency(self, nums: list[int], k: int) -> list[int]:
    count = {} #create a dictionary with counts of each number
    freq = [[] for i in range(len(nums) + 1)] #creates a 'bucket list' - a list of empty lists for each item in our number list

    #Make the hashmap
    for n in nums:
        count[n] = 1 + count.get(n, 0) #increases count of specific number by 1 - if it's not there, then it initialises
    
    #Populate the bucket list
    for n, c in count.items():
        freq[c].append(n) #freq is ordered in count of numbers, so we append the relevant number to however many is counted
    
    #Output the result
    res = []
    for i in range(len(freq) - 1, 0, -1): #creates a for loop going backwards equal to the length of the bucketlist
        for n in freq[i]: #checks each list in the bucket list (backwards)
            res.append(n) #appends the list in the result
            if len(res) == k: #if we have the top k results
                return res #return res
            
#Why is this O(n)? Because nothing in this is bigger than n length.