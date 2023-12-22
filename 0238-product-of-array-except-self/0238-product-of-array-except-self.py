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
    

        length = len(nums)
        answer = [0]*length

        # left product for each element
        left = 1
        for i in range(length):
            answer[i] = left
            left *= nums[i]

        # right product for each element
        right = 1
        for i in range(length-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
        