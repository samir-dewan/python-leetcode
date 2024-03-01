def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures) #provides a separate list for each temp
    stack = [] #stack will be a pair that takes [index, value]. This will always be the highest temperature so far.

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][1]: 
        #checks that there is something in the stack and 
        #the value is higher than the most recent stack entry temp
            
            stackInd, stackT = stack.pop() #pops the stack value into two values
            res[stackInd] = (i - stackInd) #changes the result of the relevant index to be the numbers of indexes away the stack previous was
        stack.append([i, t]) #creates a new stack with the new temp and index
        print(stack)

    return res 

print(dailyTemperatures([70, 71, 69, 65, 70, 72, 73]))