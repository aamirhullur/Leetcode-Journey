class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()
        # for i,r in enumerate((nums)):
        for i in range(0,len(nums)-2):
            e = nums[i]
            target = nums[i]*-1
    
            l,r = i+1, len(nums)-1
            while l < r:
                curSum = nums[l] + nums[r]
                if curSum > target:
                    r-=1
                elif curSum < target:
                    l+=1
                elif curSum == target:
                    res.add((e, nums[l], nums[r])) 
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l+=1
                    r-=1
        return [list(item) for item in res]