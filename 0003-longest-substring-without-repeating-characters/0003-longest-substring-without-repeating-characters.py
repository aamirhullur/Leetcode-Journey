class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hmap and l < r:
                # hmap[s[l]] -= 1
                hmap.pop(s[l])
                l+=1
            hmap[s[r]] = 1

            res = max(res, sum(hmap.values()))
        return res



