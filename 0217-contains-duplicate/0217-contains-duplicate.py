class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
#         for i in range(0,len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     return(True)
#                 else:
#                     continue
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False
        