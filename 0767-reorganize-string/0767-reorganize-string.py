class Solution:
    def reorganizeString(self, s: str) -> str:
        # aaabc - > abaca
        # aabbc -> ababc
        # aaaabc -> abacaa

        # if most freq element > len(s) - rem -> return ""
        # max_heap -> pop -> append -> push

        strCnt = collections.Counter(s) # O(n)

        maxHeap = [(-v,k) for k,v in strCnt.items()] # O(n)
        heapq.heapify(maxHeap) # log(n)

        freq = -maxHeap[0][0]
        rem = len(s) - freq

        if freq > rem+1:
            return ""

        res = []   

        q = collections.deque()
        time = 1
        while maxHeap or q:
            while q and q[0][0] == time:
                t,c,val = q.popleft()
                heapq.heappush(maxHeap,(c,val))

            cnt, s = heapq.heappop(maxHeap) # log(n)
            res.append(s)
            cnt += 1
            if cnt:
                q.append((time+2,cnt,s))

            time += 1
        return ''.join(res)