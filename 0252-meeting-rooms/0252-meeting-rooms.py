class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort()
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if prevEnd <= start:
                prevEnd = end
            else:
                return False
        return True