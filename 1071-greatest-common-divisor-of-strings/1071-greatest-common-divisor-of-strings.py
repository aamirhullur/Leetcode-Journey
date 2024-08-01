class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        x = len(str1)
        y = len(str2)
        if str1 + str2 != str2 + str1 :
            return ''
        while y!=0:
            x,y = y,x%y
        return str1[:x]