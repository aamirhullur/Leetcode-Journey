class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height)-1

        while l<r:
            H = min(height[l],height[r])
            W = r-l
            area = H*W
            res = max(res,area)

            if height[l] <= height[r]:
                l+=1
            else:
                r-=1

        return res'