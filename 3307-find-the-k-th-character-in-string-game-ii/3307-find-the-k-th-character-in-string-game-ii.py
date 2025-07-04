# class Solution:
#     def kthCharacter(self, k: int, operations: List[int]) -> str:
        
#         s="a"
#         while len(s) < k:
#             ns = []

#             for o in operations:
#                 if o == 0:
#                     s = s+s
#                 else:
#                     ns = ""
#                     print(len(s))
#                     for c in s:
#                         if ord(c) + 1 == 123:
#                             ns = ns + (chr(ord('a')))
#                         else:
#                             ns = ns + (chr(ord(c) + 1))
#                     s = s + ns
#         return s[k-1]

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1
        return chr(ord("a") + (ans % 26))
