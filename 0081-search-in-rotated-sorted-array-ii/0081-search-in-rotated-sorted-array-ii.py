class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return(True)
            else:
                continue
                
        return(False)
            
        