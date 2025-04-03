# class Solution:
#     def maximumTripletValue(self, nums: List[int]) -> int:
        # res = 0
        # currSum = nums[0]

        # for i in range(1,len(nums)-1):
        #     # print([currSum,nums[i],i])
        #     if currSum - nums[i] < 0:
        #         currSum = nums[i]
        #     else:
        #         calc = (currSum - nums[i]) * max(nums[i+1:])
        #         res = max(res,calc)
        
        # return res

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res