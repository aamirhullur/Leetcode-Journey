class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            hmap[s[r]] += 1
            while (r-l+1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                if hmap[s[l]] == 0:
                    hmap.pop(s[l])
                l+=1
            
            res = max(res,(r-l+1))

        return res
