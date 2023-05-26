class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == ')' and stack[-1] != '(': return False
                elif c == ']' and stack[-1] != '[': return False
                elif c == '}' and stack[-1] != '{': return False
                else:
                    stack.pop()
        # return empty stack as true or if stack having any data as false
        return not stack
        
            
