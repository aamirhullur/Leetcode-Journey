class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        d = {5:0,10:0,20:0}
    
        for i,r in enumerate(bills):
            d[r] += 1
    
            if r == 10:
                if d[5]:
                    d[5] -= 1
                else:
                    return False
            if r == 20:
                if d[10] and d[5]:
                    d[10]-=1
                    d[5]-=1
                elif d[5] > 2:
                    d[5] -= 3
                else:
                    return False
                
        return True