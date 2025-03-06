class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=set()
        nums.sort()

        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                t = (nums[i] + nums[j]) * -1
                new_target = target + t
                l,r = j+1, len(nums)-1

                while l<r:
                    if nums[l] + nums[r] > new_target:
                        r-=1
                    elif nums[l] + nums[r] < new_target:
                        l+=1
                    else:
                        res.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
                        while nums[l] == nums[l-1] and l < r:
                            l+=1
                    
        return [i for i in res]