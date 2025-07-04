class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        maxHeap = [[-v,k] for k,v in Counter(tasks).items()]
        
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        res = 0
        while maxHeap or q:
            time+=1
            if maxHeap:
                val,task = heapq.heappop(maxHeap)
                val += 1
                if val != 0:
                    q.append((time+n,val,task))
            else:
                time = q[0][0]
            if q and q[0][0] == time:
                (t,val1,task1) = q.popleft()
                heapq.heappush(maxHeap, [val1,task1])
        return time
