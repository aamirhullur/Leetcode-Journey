class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            if len(heap) >= k:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res