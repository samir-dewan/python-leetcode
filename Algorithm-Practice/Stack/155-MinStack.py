class MinStack:

    def __init__(self) -> None:
        self.stack = []
        self.minStack = [] #will create a stack that always has the minimum number as top

    def push(self, val) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) #creates the most minimum number
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() #this works because the minimum number will repeat for however many number of times

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]