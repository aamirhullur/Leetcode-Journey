class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0] * len(nums)
        curr1, curr2 = 1,1
        for i in range(len(nums)):
            prefix.append(curr1)
            suffix[len(nums)-1-i] = curr2
            curr1 *= nums[i]
            curr2 *= nums[len(nums)-1-i]
            
        return [prefix[i]*suffix[i] for i in range(len(nums))]