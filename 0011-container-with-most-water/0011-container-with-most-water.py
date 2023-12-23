class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l , r = 0 , len(height) -1 
        while r - l > 0:
            # print(l,r)
            print(height[l],height[r])
            # area = min(height[i-1],height[j-1]) * abs(i-j)
            area = min(height[l], height[r]) * (r-l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            elif height[r] == height[l]:
                if height[l+1] > height[r-1]:
                    l+=1
                else:
                    r-=1
        return res
