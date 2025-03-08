class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        curr = 0
        maxAvg = float('-inf')
        for r in range(len(nums)):
            curr += nums[r]

            if r-l+1 == k:
                avg = curr/k
                maxAvg=max(avg,maxAvg)
                curr-=nums[l]
                l+=1
        return maxAvg