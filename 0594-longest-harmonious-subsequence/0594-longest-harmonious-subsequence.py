class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for r in freq:
            if r - 1 in freq:
                res = max(res, freq[r]+freq[r-1])
        return res




