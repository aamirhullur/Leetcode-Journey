class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def helper(n):
            return 0 if nums[n] else 1

        res = 0
        for i in range(len(nums)-2):
            if not nums[i]:
                nums[i] = 1
                nums[i+1] = helper(i+1)
                nums[i+2] = helper(i+2)
                res+=1
        if not nums[-1] or not nums[-2]:
            return -1
        
        return res