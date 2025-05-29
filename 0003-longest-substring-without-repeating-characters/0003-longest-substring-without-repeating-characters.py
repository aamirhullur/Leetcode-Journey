class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l = 0
        hmap = {}
        res = 0
        for r in range(len(s)):
            while s[r] in hmap:
                hmap[s[l]] -= 1
                if hmap[s[l]] == 0:
                    hmap.pop(s[l])
                l+=1
            hmap[s[r]] = 1
            res = max(res, r-l+1)
        return res
                
                
            
                