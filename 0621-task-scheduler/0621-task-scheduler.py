class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        timer = 0
        q = deque()
        while maxHeap or q:
            timer += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,timer+n])
            else:
                timer = q[0][1]
            
            if q and q[0][1] == timer:
                heapq.heappush(maxHeap,q.popleft()[0])

        return timer