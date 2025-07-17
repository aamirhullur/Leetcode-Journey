class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, -1*num)

        if self.minHeap and self.maxHeap and (self.maxHeap[0] < (-1*self.minHeap[0])):
            heapq.heappush(self.maxHeap, -1*heapq.heappop(self.minHeap))
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -1*heapq.heappop(self.minHeap))
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -1*heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:

        if len(self.minHeap) == len(self.maxHeap):
            val1 = -1*self.minHeap[0]
            val2 = self.maxHeap[0]
            return (val1+val2)/2
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return -1*self.minHeap[0]
            else:
                return self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()