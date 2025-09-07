class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            left = [-i for i in range(1,n//2 + 1)]
            right = [i for i in range(1,n//2 + 1)]
            arr = left + right 
            return arr
        else:
            n = n-1
            left = left = [-i for i in range(1,n//2 + 1)]
            right = [i for i in range(1,n//2 + 1)]
            return left + [0] + right