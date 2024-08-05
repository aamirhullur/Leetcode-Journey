class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        d = {}
        
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for j in arr:
            if d[j] == 1:
                k-=1
                
            if k == 0:
                return j
        
        return ""
        