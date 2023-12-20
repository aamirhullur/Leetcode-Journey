class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}

        for i, num in enumerate(nums):
            # print(dictionary)
            c = target - num
            if c in dictionary:
                return [dictionary[c],i]
            dictionary[num] = i
                
        