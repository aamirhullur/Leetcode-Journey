class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # L,R = 0, len(nums)-1
        # res = nums[0]

        # while L <= R:
        #     if nums[L] < nums[R]:
        #         res = min(res, nums[L])
        #         break

        #     m = (L + R)//2
        #     res = min(res, nums[m])
        #     if nums[m] >= L:
        #         L = m+1
        #     else:
        #         R = m-1
        
        # return res

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
