class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        res = bin(num)[2:]
        new = ""
        for i in res:
            if i == "1":
                new += '0'
            else:
                new += '1'
        return(int(new,2))