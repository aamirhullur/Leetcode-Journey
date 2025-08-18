class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums)+1)
        postfix = [0] * (len(nums)+1)

        N = len(nums)

        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
            postfix[N-i-1] = postfix[N-i] + nums[N-i-1]
        
        print(prefix,postfix)
        for i in range(len(nums)):
            if prefix[i] == postfix[i+1]:
                return i
        return -1
        
