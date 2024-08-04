class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        arr = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    arr.append(nums[i])
                else:
                    arr.append(sum(nums[i:j+1]))
        arr = sorted(arr)
        a=10**9+7
        return (sum(arr[left-1:right]))%a
                