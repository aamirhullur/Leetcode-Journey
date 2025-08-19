class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = float('inf')
        while l<=r:
            val = 0
            m = (l+r)//2

            for i in range(len(piles)):
                val += ceil(piles[i]/m)
            
            if val <= h:
                res = min(res, m)
                r = m-1
            else:
                l = m+1 
        return res