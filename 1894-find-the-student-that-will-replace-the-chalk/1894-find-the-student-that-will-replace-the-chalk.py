class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        
        temp = k%sum(chalk)
        for i in range(len(chalk)):
            temp -= chalk[i]
            if temp < 0:
                return i