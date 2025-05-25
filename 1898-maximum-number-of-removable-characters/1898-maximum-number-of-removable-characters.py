class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def isSub():
            i1,i2 = 0,0
            while i1 < len(s) and i2<len(p):
                if i1 in remove or s[i1] != p[i2]:
                    i1+=1
                    continue
                i1+=1
                i2+=1
            return i2 == len(p)

        l,r = 0,len(removable)-1
        res = 0
        while l<=r:
            m = (l+r)//2
            remove = set(removable[:m+1])
            if isSub():
                res = max(res,m+1)
                l=m+1
            else:
                r=m-1
        return res
