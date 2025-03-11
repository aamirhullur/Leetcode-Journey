class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        l = 0
        hmap = defaultdict(int)
        res = 0
        for r in range(len(s)):
            hmap[s[r]] += 1
            while len(hmap) == 3:
                res+= len(s) - r
                # while 
                hmap[s[l]]-=1
                if hmap[s[l]]==0:
                    hmap.pop(s[l])
                l+=1
        return res
