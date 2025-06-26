class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        def find_bit_len(val):
            num = 0
            while val:
                num += 1
                val//=2
            return num

        
        currNum = 0
        bits = find_bit_len(k)
        res = 0

        for idx, ch in enumerate(s[::-1]):
            if ch == '0':
                res += 1
            else:
                if idx < bits and currNum + 2**idx <= k:
                    currNum += 2**idx
                    res += 1
        return res


