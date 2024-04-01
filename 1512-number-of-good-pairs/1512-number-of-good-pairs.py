class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        res = 0
        for i,r in c.items():
            res += r * (r-1) // 2
        return res
        