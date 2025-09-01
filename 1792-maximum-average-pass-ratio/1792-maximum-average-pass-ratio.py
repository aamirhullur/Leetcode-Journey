class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t
        
        arr = [(-gain(p,t),p,t) for p,t in classes]
        heapq.heapify(arr)

        while extraStudents:
            ratio,passingStudents,totalStudents = heapq.heappop(arr)
            passingStudents+=1
            totalStudents+=1
            heapq.heappush(arr, (-gain(passingStudents,totalStudents),passingStudents,totalStudents))
            extraStudents-=1
        
        print(arr)
        res = 0
        for r,p,t in arr:
            res += p/t
        
        return res / len(arr)
