def BinarySearch(target: int, nums: list[int]) -> int:
    l, r = 0, len(nums) - 1

    while l <= r: #equals in case nums is of one number
        m = (l + r) // 2 #returns the midpoint between two points
        if nums[m] < target:
            l = m + 1 #moves the goalpost so m is bigger
        elif nums[m] > target:
            r = m - 1 #moves the goalpost so m is smaller
        else:
            return m
    
    return -1