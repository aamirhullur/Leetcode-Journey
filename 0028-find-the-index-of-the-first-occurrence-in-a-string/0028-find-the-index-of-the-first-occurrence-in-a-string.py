class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j = 0,0

        while i< len(haystack) and j < len(needle):
            while i < len(haystack) and haystack[i] != needle[j] :
                i+=1
            
            tmp1,tmp2 = i, j

            while i<len(haystack) and j<len(needle) and haystack[i] == needle[j]:
                i+=1
                j+=1
                if j == len(needle):
                    return tmp1
            j = tmp2
            i = tmp1+1

        return -1
            