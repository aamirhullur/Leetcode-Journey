class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = defaultdict(int)
        for i in range(len(s1)):
            h1[s1[i]] += 1

        for r in range(0,len(s2)-len(s1)+1):
            if s2[r] in h1:
                if Counter(s2[r:r+len(s1)]) == h1:
                    return True
        
        return False



