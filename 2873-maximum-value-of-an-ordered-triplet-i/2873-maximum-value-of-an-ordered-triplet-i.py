class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        currI = nums[0]
        for i in range(1,len(nums)-1):
            if currI - nums[i] < 0:
                currI = nums[i]
            else:
                calc = (currI - nums[i]) * max(nums[i+1:])
                if calc < 0:
                    calc = 0
                res = max(res, calc)

        return res
