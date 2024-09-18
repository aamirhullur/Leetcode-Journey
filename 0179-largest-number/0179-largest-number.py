# class Solution(object):
#     def largestNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: str
#         """
        
#         # res = []
#         # for i in nums:
#         #     a = [int(i) for i in list(str(i))]
#         #     res = res + a
#         # res = sorted(res, reverse=True)
#         # x = ''.join(str(x) for x in res)
#         # return x
#         res = []
#         for i in nums:
#             res.append(str(i))


#         res = sorted(res,reverse=True)
#         a = ''.join(x for x in res)
#         return a

class Solution(object):
    def compare(self, a, b):
        if str(a) + str(b) > str(b) + str(a):
            return -1
        else:
            return 1

    def largestNumber(self, nums):
        sorted_nums = sorted(nums, key=cmp_to_key(self.compare))

        # Convert the sorted numbers to a single string
        string_nums = ''.join(str(num) for num in sorted_nums)

        if string_nums[0] == '0':
            return '0'
            
        return string_nums
