class Solution:
    def isValid(self, s: str) -> bool:
        hmap =  {')' : '(',
                ']' : '[',
                '}' : '{'}
        stack = []

        for i in range(len(s)):
            if s[i] in hmap:
                if stack and stack[-1] == hmap[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            

            
        
        return False if stack else True