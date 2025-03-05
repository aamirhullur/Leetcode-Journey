class Solution:
    def coloredCells(self, n: int) -> int:
        res = 0
        while n>=0:
            if n > 0:
                res += 4 * (n-1) 
            else: 
                res += 1
            n-=1
        
        return res