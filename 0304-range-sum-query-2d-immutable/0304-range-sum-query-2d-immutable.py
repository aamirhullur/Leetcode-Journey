class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0]*len(matrix[0]) for _ in range(len(matrix))]\

        for row in range(len(matrix)):
            self.currSum = 0
            for n in range(len(matrix[0])):
                self.currSum += matrix[row][n]
                self.prefix[row][n] = self.currSum
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        rows = abs(row1 - row2) + 1
        res = 0
        for i in range(row1,row2+1):
            res += self.prefix[i][col2] - (self.prefix[i][col1-1] if col1>0 else 0)

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)