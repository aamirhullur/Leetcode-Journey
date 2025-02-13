class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)  # Sort in descending order
        cnt = 0
        
        while len(nums) > 1 and nums[-1] < k:
            cnt += 1
            i, j = nums.pop(), nums.pop()
            calc = (i * 2) + j
            
            l, r = 0, len(nums)
            # Find correct insertion point to maintain descending order
            while l < r:
                mid = (l + r) // 2
                if mid < len(nums) and nums[mid] > calc:
                    l = mid + 1
                else:
                    r = mid
                    
            nums.insert(l, calc)
        
        return -1 if nums[-1] < k else cnt
