class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        N = len(intervals)
        if N == 1:
            return intervals 
            
        intervals.sort()
        res = [intervals[0]]

        for start,end in intervals[1:]:
            old_start, old_end = res[-1]
            if start <= old_end:
                res.pop()
                start = min(start,old_start)
                end = max(end,old_end)
            res.append((start,end))

        return res
