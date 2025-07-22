class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        # for l in range(len(nums)):
        #     hmap = set()
        #     r = l
        #     cnt = 0
        #     while r < len(nums) and nums[r] not in hmap:
        #         hmap.add(nums[r])
        #         cnt+=nums[r]
        #         r+=1
        #     l = r-1
        #     res = max(res,cnt)

        # return res

        l = 0   
        hmap = {}
        curr_sum = 0
        res = 0
        for r in range(len(nums)):                
            while nums[r] in hmap:
                hmap[nums[l]] -= 1
                curr_sum -= nums[l]
                if not hmap[nums[l]]:
                    hmap.pop(nums[l])
                l+=1
            hmap[nums[r]] = 1
            curr_sum += nums[r]
            res = max(res,curr_sum)
        return res
            

