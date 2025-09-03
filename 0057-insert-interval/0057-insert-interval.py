class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if not intervals:
        #     return [newInterval]
        
        res = []
        for i in range(len(intervals)):
            start,end = intervals[i]
            if newInterval[1] < start:
                res = res + [newInterval] + intervals[i:]
                return res
            elif newInterval[0] > end:
                res.append([start,end])
            else:
                newInterval = [min(start,newInterval[0]), max(end,newInterval[1])]
        
        res.append(newInterval)
        return res