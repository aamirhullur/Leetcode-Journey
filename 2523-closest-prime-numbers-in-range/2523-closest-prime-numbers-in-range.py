class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            if n == 1 or n ==2 :
                return True
            if n % 2 == 0:
                return False
            for i in range(3,n,2):
                if n % i == 0:
                    return False
            return True
        
        diff = float('inf')

        l = left
        while l < right:
            if l == 1:
                l+=1
                continue
            if is_prime(l):
                r = l+1
                while r < right and not is_prime(r):
                    r+=1
                    if r == right and not is_prime(r):
                        l = r+1
                        break
                if is_prime(r) and r - l < diff:
                    diff = r-l
                    res = [l,r]
                    if diff <= 3:
                        return res
                l=r-1
            l+=1

        return res if diff != float('inf') else [-1,-1]