class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prefix = []
        total = 0

        for i in nums:
            total += i
            prefix.append(total)
        
        R = len(nums) - 1
        for i in range(len(nums)):
            
            if i < 1:
                left = 0
            else:
                left = prefix[i-1]
            L = i
            right = prefix[R] - prefix[L]
             
            if left == right:
                return i
        return -1
        
