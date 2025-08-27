class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 2

        # [1,5,8,4,7,6,5,3,1]
        while i >= 0 and nums[i+1] <= nums[i]:
            i-=1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j-=1
            # nums[i], nums[j] = nums[j],nums[i]
            self.swap(nums,i,j)
        self.reverse(nums,i+1)
            # print(nums)
            # print(nums[i+1:])

    def reverse(self,nums,l):
        r = len(nums)-1
        while l<r:
            self.swap(nums,l,r)
            l+=1
            r-=1

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
