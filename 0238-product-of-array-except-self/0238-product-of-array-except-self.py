class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#         res = [1] * len(nums)

#         for i,r in enumerate(nums):
#             pre = nums[:i]
#             post = nums[i+1:]
#             left,right = 1,1
#             if len(pre) > 0:
#                 left = reduce(lambda x, y: x*y, pre)
#             if len(post) > 0:
#                 right = reduce(lambda x, y: x*y, post)
#             res[i] = left*right

#         return(res)
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)
        