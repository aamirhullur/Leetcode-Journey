class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        total = row * col
        l,r = 0,total-1

        while l<=r:

            m = (l + r)//2
            row_num = m // col
            col_num = m % col
            if matrix[row_num][col_num] < target:
                l = m + 1
            elif matrix[row_num][col_num] > target:
                r = m - 1
            else:
                return True

        return False
        