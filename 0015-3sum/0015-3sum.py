class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()

        for i in range(len(nums)-2):
            prev = nums[i]
            L, R = i+1, len(nums) - 1
            target = nums[i] * -1
            while L < R:
                if nums[L] + nums[R] > target:
                    R-=1
                elif nums[L] + nums[R] < target:
                    L+=1
                else:
                    res.add((nums[i],nums[L],nums[R]))
                    L+=1
                    R-=1

        return [list(i) for i in res]