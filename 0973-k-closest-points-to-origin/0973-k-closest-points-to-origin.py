class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        arr = []
        res = []
        for idx,(x,y) in enumerate(points):
            val = x**2 + y**2
            arr.append([val,[x,y]])
        heapq.heapify(arr)
        while k:
            val = heapq.heappop(arr)
            res.append(val[1])
            k-=1
        return res