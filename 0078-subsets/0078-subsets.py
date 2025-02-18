class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr = []
        res = []
        def bt(i,arr):
            if i >= len(nums):
                res.append(list(arr))
                return

            arr.append(nums[i])
            bt(i+1, arr)

            arr.pop()
            bt(i+1, arr)

        bt(0,arr)

        return res