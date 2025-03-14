class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        if sum(candies) == k:
            return 1
        
        l,r = 1, max(candies)

        while l<=r:
            m = (l+r)//2
            kids = 0
            for c in candies:
                kids+= c//m
            
            if kids >= k:
                res = m
                l = m+1
            else:
                # res = m
                r=m-1
        #     print([m,kids,l,r,m])
        # print([m,kids])
        return res
