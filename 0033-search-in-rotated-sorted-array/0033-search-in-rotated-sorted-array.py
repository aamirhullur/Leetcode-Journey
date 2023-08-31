class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cnt = 0
        for i in range(0,len(nums)):
            if nums[i] == target:
                return(i)
            else:
                cnt+=1
                continue
        
        if cnt>=len(nums):
            return(-1)
        