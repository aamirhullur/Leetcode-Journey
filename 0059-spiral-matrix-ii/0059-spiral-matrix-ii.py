class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        cnt = 1
        matrix = [[0]*n for _ in range(n)]
    
        l ,r = 0, len(matrix[0])
        t, b = 0, len(matrix)
    
        while l < r and t < b:
            
            for i in range(l,r):
                matrix[t][i] = cnt
                cnt+= 1
            t+= 1
    
            for i in range(t,b):
                matrix[i][r-1] = cnt
                cnt += 1
            r -= 1
    
            for i in range(r-1,l-1,-1):
                matrix[b-1][i] = cnt
                cnt+=1 
            b -= 1
    
            for i in range(b-1 ,t-1, -1):
                matrix[i][l] = cnt
                cnt += 1
            l+=1
    
        return matrix