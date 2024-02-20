def WaterWithContainer(array: list[int]) -> int:
    w = len(array) - 1
    l, r = 0, len(array) - 1
    res = 0
    while l < r:
        h = min(array[l], array[r])
        area = w * h
        res = max(area, res)
        if array[l] < array[r]:
            l += 1
        else:
            r -= 1
        w -= 1
    
    return res