class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = set()

        def bt(j,arr):
            if len(arr) < len(nums)+1:
                res.add(tuple(arr))

            for i in range(j,len(nums)):
                arr.append(nums[i])
                bt(i+1,arr)
                arr.pop()

        nums.sort()
        bt(0,[])
        return [list(i) for i in res]