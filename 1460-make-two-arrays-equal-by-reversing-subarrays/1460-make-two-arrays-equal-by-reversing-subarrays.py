class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        d = {}
        
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    
        for i in target:
            if i in d and d[i]:
                d[i] -= 1
            else:
                return False
            
        return True
                
        