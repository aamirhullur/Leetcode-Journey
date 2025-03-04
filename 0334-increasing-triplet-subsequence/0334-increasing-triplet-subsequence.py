class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False

        first,second = float('inf'), float('inf')


        for n in range(len(nums)):

            if nums[n] <= first:
                first = nums[n]
            elif nums[n] <= second:
                second = nums[n]
            else:
                return True
        return False