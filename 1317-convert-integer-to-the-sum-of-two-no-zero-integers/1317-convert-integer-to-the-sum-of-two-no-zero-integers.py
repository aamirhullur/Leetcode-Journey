class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n-1
        b = n - a
        while '0' in str(a) or '0' in str(b):
            a-=1
            b=n-a
        
        return [a,n-a]

