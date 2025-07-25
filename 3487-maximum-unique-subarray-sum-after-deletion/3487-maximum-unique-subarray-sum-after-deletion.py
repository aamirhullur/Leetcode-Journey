class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        res = 0
        for i in range(len(nums)):
            if nums[i] not in seen and nums[i] > 0:
                seen.add(nums[i])
                res+=nums[i]
        
        return res if len(seen) > 0 else max(nums)

