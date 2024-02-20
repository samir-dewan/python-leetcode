def ThreeSum(array: list[int]) -> list:
    res = []
    array.sort()

    for i, a in enumerate(array):
        if i > 0 and a == array[i - 1]:
            continue #looks for duplicate values for the first value a

        l, r = 0, len(array) - 1 #initialises two pointers
        while l < r:
            sum = a + array[l] + array[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append([a, array[l], array[r]])
                while array[l] == array[l - 1] and l < r: #looks for duplicate values for the second value l
                    l += 1
    return res