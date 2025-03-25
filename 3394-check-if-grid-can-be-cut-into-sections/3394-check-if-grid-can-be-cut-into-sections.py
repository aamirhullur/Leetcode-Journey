class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_vals = [(r[0], r[2]) for r in rectangles]
        y_vals = [(r[1], r[3]) for r in rectangles]

        x_vals.sort()
        y_vals.sort()

        def interval_func(intervals):
            cnt = 0
            prev_end = -1
            for start,end in intervals:
                if start >= prev_end:
                    cnt+=1
                
                prev_end = max(prev_end, end)
            return cnt

        return (interval_func(x_vals)>= 3 or interval_func(y_vals) >= 3)