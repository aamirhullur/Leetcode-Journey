class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # res = []
        res = set()

        def bt(arr,visited):
            if len(arr) == len(nums):
                res.add(tuple(arr))

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    arr.append(nums[i])
                    bt(arr,visited)
                    visited.remove(i)
                    arr.pop()    

        bt([],set())

        return [list(i) for i in res]
