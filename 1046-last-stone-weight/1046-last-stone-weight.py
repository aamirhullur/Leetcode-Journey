class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)

            if x!=y:
                heapq.heappush(stones, -1*(y-x))

        return stones[0]*-1 if len(stones)!= 0 else 0
