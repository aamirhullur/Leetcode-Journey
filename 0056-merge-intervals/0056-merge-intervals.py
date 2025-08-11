class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort()

        prev = intervals[0]

        for i in range(1,len(intervals)):
            if intervals[i][0] > prev[1]:
                res.append(prev)
                prev = intervals[i]
            else:
                prev = [min(intervals[i][0],prev[0]), max(intervals[i][1],prev[1])]
        res.append(prev)
        return res