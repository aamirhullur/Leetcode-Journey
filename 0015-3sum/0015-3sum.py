class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1
            target = -nums[i]
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    res.append((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res