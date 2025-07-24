class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        first = (x, "ab")
        second = (y, "ba")

        if x < y:
            first, second = second, first

        res = 0
        for p, ss in [first,second]:
            stack = []
            for c in s:
                stack.append(c)
                if len(stack) > 1 and stack[-1] == ss[1] and stack[-2] == ss[0]:
                    res += p
                    stack.pop()
                    stack.pop()
            s = ''.join(stack)
        
        return res
