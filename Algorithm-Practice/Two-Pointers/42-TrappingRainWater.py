def TrappingRainWater(height: list[int]) -> int:
    if not height: return 0

    l, r = 0, len(height) - 1 #creates two pointers
    leftMax, rightMax = height[l], height[r] #checks for the highest points (that would allow for the edges of water retention)
    res = 0 #initialises result

    while l < r:
        if leftMax < rightMax: #if the lhs of the container bounds the potential volume
            l += 1 #move the left counter along
            leftMax = max(leftMax, height[l]) #change the leftmax if there is a bigger bound
            res += leftMax - height[l] #if there is a space between the bound and the current height space, add it to the result

        else: #if the rhs of the container bounds...same thing
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res #return the result