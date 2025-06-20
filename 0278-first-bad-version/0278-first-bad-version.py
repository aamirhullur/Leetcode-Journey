# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l,r = 1, n

        while l<r:
            m = (l+r)//2

            if not isBadVersion(m):
                l=m+1
            elif isBadVersion(m):
                r=m
        return r