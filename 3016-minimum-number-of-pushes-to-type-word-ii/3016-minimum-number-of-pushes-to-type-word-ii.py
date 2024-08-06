class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        d = {}
    
        for i,r in enumerate(word):
            if r in d:
                d[r] += 1
            else: 
                d[r] = 1
    
        sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
        print(d)
        res = 0
        cnt = 0
        for e, (i,r) in enumerate(sorted_items):
            if e % 8 == 0:
                cnt+=1
            res = res + (cnt * r)
        return res
        