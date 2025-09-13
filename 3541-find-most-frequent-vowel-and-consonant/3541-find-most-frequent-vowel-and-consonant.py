class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        hmap = defaultdict(int)
        vow_max = 0
        con_max = 0

        for i in s:
            hmap[i] += 1
            if i in 'aeiou':
                if hmap[i] > vow_max:
                    vow_max = hmap[i]
            else:
                if hmap[i] > con_max:
                    con_max = hmap[i]
        return vow_max + con_max