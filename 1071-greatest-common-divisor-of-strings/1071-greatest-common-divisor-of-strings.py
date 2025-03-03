class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # if str1 + str2 != str2 + str1:
        #     return ""
        
        # return str1[0:gcd(len(str1), len(str2))]

        if str1 + str2 != str2 + str1:
            return ""

        len1, len2 = len(str1), len(str2)

        def isDivisor(n: int) -> bool:
            if len1 % l == 0 and len2 % l == 0:
                return True if str1[:l] == str2[:l] else False
            else:
                return False 

        for l in range(min(len1,len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""