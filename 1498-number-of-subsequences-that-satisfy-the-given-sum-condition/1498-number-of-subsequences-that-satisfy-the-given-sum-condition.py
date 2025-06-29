class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums)-1
        res = 0
        mod = 10**9 + 7
        nums.sort()

        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + 2**(r-l))% mod
                l+=1
            else:
                r-=1
        return res