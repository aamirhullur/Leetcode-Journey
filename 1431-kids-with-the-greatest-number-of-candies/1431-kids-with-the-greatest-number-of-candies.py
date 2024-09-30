class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        a = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                a.append(True)
            else:
                a.append(False)
                
        return a