class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    currSum = nums[i] + nums[j] 
                    if currSum == target:
                        return[i,j]
                    else:
                        continue
        
