class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp = {}
        for i,r in enumerate(nums):
            if r in temp:
                temp[r] += 1
            else:
                temp[r] = 1

        res = dict(sorted(temp.items(), key = lambda x: x[1], reverse = True)[:k])

        res1 = list(res.keys())

        return(res1)
