class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            i, j = (-1 * heapq.heappop(stones)), (-1* heapq.heappop(stones))
            if i != j:
                z = i - j
                heapq.heappush(stones,(-1*z))
        
        # return (-1*s[-1]) if stones else 0
        return -1*stones[0] if stones else 0


