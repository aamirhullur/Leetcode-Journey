class Solution(object):
    def numberOfPairs(self, points):
        points.sort(key=lambda p:(p[0],-p[1]))
        c=0
        for i,(xi, yi) in enumerate(points):
            b=float('-inf')
            for xj, yj in points[i+1:]:
                if yi>=yj>b:
                    c+=1
                    b=yj
        return c