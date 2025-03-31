class Solution:
    def removeStars(self, s: str) -> str:
        # stack = []

        # for i in range(len(s)):
        #     if s[i] == '*':
        #         stack.pop()
        #     else:
        #         stack.append(s[i])
        # return ''.join(stack)


        l = 0
        s = list(s)

        for r in range(len(s)):
            if s[r] == '*':
                l-=1
            else:
                s[l] = s[r]
                l+=1
                
        return ''.join(s[:l])