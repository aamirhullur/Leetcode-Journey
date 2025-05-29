class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        h1 = {}
        for i in range(len(s1)):
            h1[s1[i]] = 1 + h1.get(s1[i],0)
        
        for r in range(len(s2)-len(s1)+1):
            if Counter(s2[r:r+len(s1)]) == h1:
                return True

        return False


                