class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # n = len(intervals)
        # res = []
        # for q in queries:
        #     cur = -1
        #     for l, r in intervals:
        #         if l <= q <= r:
        #             if cur == -1 or (r - l + 1) < cur:
        #                 cur = r - l + 1
        #     res.append(cur)
        # return res

        minHeap = []
        res,i = {}, 0

        intervals.sort()

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i+=1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[i] for i in queries]

