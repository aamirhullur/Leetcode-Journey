class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m*n != len(original):
            return []
        
#         res = [[0]*n for _ in range(m)]
        
#         for i in range(m):
#             res[i] = original[n*i:n*(i+1)]
#         return res

        # res = [original[n*i:n*(i+1)] for i in range(m)]
        return [original[n*i:n*(i+1)] for i in range(m)]