def ValidParentheses(s: str) -> bool:
        stack = [] #create a stack
        cToO = {")": "(", "}":"{", "]":"["} #required accompanying set hashmap
        for c in s:
            if c in cToO:
                if stack and stack[-1] == cToO[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False