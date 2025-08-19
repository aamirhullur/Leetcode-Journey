class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1

        maxL, maxR = height[l],height[r]
        res = 0

        while l<r:
            if maxL < maxR:
                res += max((maxL - height[l]),0)
                l+=1
                maxL = max(height[l],maxL)
            else:
                res += max((maxR - height[r]),0)
                r-=1
                maxR = max(height[r],maxR)
        return res
    
    
        # N = len(height)
        # maxL = [0]*N
        # maxR = [0]*N

        # maxL[0] = height[0]
        # maxR[N-1] = height[N-1]

        # for i in range(1,N):
        #     maxL[i] = max(height[i],maxL[i-1])

        # for i in range(N-2,-1,-1):
        #     maxR[i] = max(height[i],maxR[i+1])

        # res = 0
        # for i in range(N):
        #     res += min(maxL[i], maxR[i]) - height[i]
        # return res