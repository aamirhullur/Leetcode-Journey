class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        l = 0
        res = 0
        num_zeros = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > 1:
                if nums[l] == 0:
                    num_zeros -= 1
                l+=1

            res = max(res, r-l+1)
        
        return res-1 if res else 0