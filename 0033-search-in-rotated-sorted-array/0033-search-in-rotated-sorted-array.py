class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L,R = 0, len(nums)-1

        while L<R:
            m = (L+R)//2

            if nums[m] > nums[R]:
                L = m+1
            else:
                R = m

        pivot = L
        if target <= nums[len(nums)-1]:
            L,R = pivot, len(nums)-1
        else:
            L,R = 0, pivot-1
        while L<=R:
            m = (L+R)//2

            if target > nums[m]:
                L = m+1
            elif target < nums[m]:
                R = m-1
            else:
                return m
        
        return -1
