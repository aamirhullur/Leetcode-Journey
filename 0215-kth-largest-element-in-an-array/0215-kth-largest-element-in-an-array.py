class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # H = []
        
        # for i in range(len(nums)):
        #     heapq.heappush(H,nums[i])

        #     if len(H) > k:
        #         heapq.heappop(H)
        
        # return H[0]
        nums = [-s for s in nums]
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res