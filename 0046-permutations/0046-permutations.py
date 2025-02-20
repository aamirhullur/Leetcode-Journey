class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        
        def bt(arr):
            if len(arr) == len(nums):
                res.append(list(arr))

            for j in range(0,len(nums)):
                if nums[j] not in arr:
                    arr.append(nums[j])
                    bt(arr)
                    arr.pop()
            

        bt([])
        return res