class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        # small, large = [], []
        # res = []
        # for i in range(len(nums)):
        #     heapq.heappush(small,-1*nums[i])
        #     if small and large and (-1*small[0]) > large[0]:
        #         heapq.heappush(large, -1 * heapq.heappop(small))
            
        #     if len(small) > len(large) + 1:
        #         heapq.heappush(large, -1*heapq.heappop(small))
        #     if len(large) > len(small) + 1:
        #         heapq.heappush(small, -1*heapq.heappop(large))
        #     print(small, large)
        #     if len(small) + len(large) == k:
        #         print("here",i)
        #         if len(small) > len(large):
        #             res.append(-1 * small[0])
        #         elif len(large) > len(small):
        #             res.append(large[0])
        #         else:
        #             median = ((-1 * small[0]) + (large[0]))/2
        #             res.append(median)
        #     if len(small) + len(large) > k:
        #         val = nums[i-k]
        #         if val <= -1*small[0]:
        #             small.remove(-val)
        #             heapq.heapify(small)
        #             print("removed",small)
        #         else:
        #             large.remove(val)
        #             heapq.heapify(large)
        # return res


        minHeap, maxHeap = [], []
        heapDict = collections.defaultdict(int)

        res = []

        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

            if len(minHeap) > len(maxHeap):
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        
        if k % 2 == 0:
            median = ((-maxHeap[0] + minHeap[0])/2)
        else:
            median = -maxHeap[0]
        
        res.append(median)

        for i in range(k,len(nums)):
            prev = nums[i-k]
            heapDict[prev] += 1

            balance = -1 if prev <= median else 1

            if nums[i] <= median:
                balance += 1
                heapq.heappush(maxHeap, -nums[i])
            else:
                balance -= 1
                heapq.heappush(minHeap, nums[i])

            if balance < 0:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
            elif balance > 0:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))

            while maxHeap and heapDict[-maxHeap[0]] > 0:
                heapDict[-maxHeap[0]] -= 1
                heapq.heappop(maxHeap)

            while minHeap and heapDict[minHeap[0]] > 0:
                heapDict[minHeap[0]] -= 1
                heapq.heappop(minHeap)

            if k % 2 == 0:
                median = ((-maxHeap[0] + minHeap[0])/2)
            else:
                median = -maxHeap[0]
        
            res.append(median)
            
        return res
            