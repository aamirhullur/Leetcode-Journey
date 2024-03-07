class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
#         if len(s) == 1:
#             return 1
#         elif len(s) == 0:
#             return 0
#         l,r = 0,1
#         res = 0
#         cnt = 1
#         while r < len(s):
#             # print(f"{cnt} {res}")
#             if s[r] in s[l:r]:
#                 res = max(cnt,res)
#                 cnt = 0
#                 l += 1
#                 r = l
#             cnt += 1
#             r += 1
#         res = max(cnt,res)
#         return res
    
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        l,r = 0,1
        res = 0
        cnt = 1
        while r < len(s):
            if s[r] not in s[l:r]:
                cnt+=1
            else:
                res = max(cnt,res)
                cnt = 1
                l += 1
                r = l
            r+=1
            # print(f'r: {r},cnt: {cnt}')
        res = max(cnt,res)        
    
        return res
    
    