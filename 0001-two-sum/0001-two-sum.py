class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             res.append(i)
        #             res.append(j)
        # return res

        dict = {}
    
        for i, nums in enumerate(nums):
            c = target - nums
            if c in dict: 
                return[dict[c],i]
            dict[nums] = i