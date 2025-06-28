class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        s = sorted(enumerate(nums), key = lambda x: (-x[1], x[0]))
        s = sorted(s[:k], key = lambda x: x[0])
        print(s)
        return([x[1] for x in s[:k]])
