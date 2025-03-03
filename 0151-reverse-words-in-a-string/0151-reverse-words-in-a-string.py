class Solution:
    def reverseWords(self, s: str) -> str:
        # res = []
        # idx = 0
        # for i in range(len(s)+1):
        #     if  i == len(s) or s[i].isspace():
        #         if s[idx:i]:
        #             res.append(s[idx:i]) 
        #         idx=i+1
        # print(res)
        # return ' '.join(res[::-1])

        return " ".join(s.split()[::-1])
