class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we are looking for an answer where if nums[a] + nums[b] == target, return [a, b].

#original answer, with no help.
        for i, iVal in enumerate(nums):
                for j, jVal in enumerate(nums):
                    if iVal + jVal == target and j != i:
                        return [i, j]

#hashmap answer, with youtube help.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[j] = i
            #if target - j is in the hashmap, then return [hashmapKey, i]
            #else add an entry [j, i] into the hashmap