class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = Counter(nums)

        maxHeap = [(-v,k) for k,v in countMap.items()]
        heapq.heapify(maxHeap)
        res = []
        while k:
            val,key = heapq.heappop(maxHeap)
            res.append(key)
            k-=1

        return res