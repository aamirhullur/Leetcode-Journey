class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = float('-inf')
        L, R = 0, len(height) - 1
        W = 0
        while L < R:
            if height[L] < height[R]:
                W = (R-L)*height[L]
                L +=1
            else:
                W = (R-L)*height[R]
                R -=1
            maxWater = max(maxWater, W)
        return maxWater