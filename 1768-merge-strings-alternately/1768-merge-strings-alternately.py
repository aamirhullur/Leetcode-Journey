class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = len(word1)
        j = len(word2)
        res = ""
        while i or j > 0:
            if i!= 0 :
                res += word1[-i]
                i-=1
            if j!=0:
                res+=word2[-j]
                j-=1
            
        
            
                
        return res