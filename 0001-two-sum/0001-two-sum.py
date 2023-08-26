class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsLength = len(nums)
        for idx1 in range(numsLength):
            for idx2 in range(numsLength):
                # You may not use the same element twice.
                if idx1 == idx2:
                    continue
                # Return indexes of two numbers in current iteration that add up to target
                currSum = nums[idx1] + nums[idx2]
                if currSum == target:
                    return [idx1, idx2]