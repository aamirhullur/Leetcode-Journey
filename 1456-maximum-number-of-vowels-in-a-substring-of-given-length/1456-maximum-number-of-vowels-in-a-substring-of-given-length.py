class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        res = 0
        curr = 0
        vow = 0
        for r in range(len(s)):
            if s[r] in 'aeiou':
                vow += 1
            if r-l+1 == k:
                res = max(res,vow)

                if s[l] in 'aeiou':
                    vow-=1
                l+=1
        return res