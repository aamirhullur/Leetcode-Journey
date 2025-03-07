class Solution:
    # def closestPrimes(self, left: int, right: int) -> List[int]:
        # def is_prime(n):
        #     if n == 1 or n ==2 :
        #         return True
        #     if n % 2 == 0:
        #         return False
        #     for i in range(3,n,2):
        #         if n % i == 0:
        #             return False
        #     return True
        
        # diff = float('inf')

        # l = left
        # while l < right:
        #     if l == 1:
        #         l+=1
        #         continue
        #     if is_prime(l):
        #         r = l+1
        #         while r < right and not is_prime(r):
        #             r+=1
        #             if r == right and not is_prime(r):
        #                 l = r+1
        #                 break
        #         if is_prime(r) and r - l < diff:
        #             diff = r-l
        #             res = [l,r]
        #             if diff <= 3:
        #                 return res
        #         l=r-1
        #     l+=1

        # return res if diff != float('inf') else [-1,-1]

    def _sieve(self, upper_limit):
        # Create an integer list to mark prime numbers (True = prime, False = not prime)
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime

        for number in range(2, int(upper_limit**0.5) + 1):
            if sieve[number]:
                # Mark all multiples of 'number' as non-prime
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left, right):
        # Step 1: Get all prime numbers up to 'right' using sieve
        sieve_array = self._sieve(right)

        prime_numbers = [
            num for num in range(left, right + 1) if sieve_array[num]
        ]

        # Step 2: Find the closest prime pair
        if len(prime_numbers) < 2:
            return -1, -1  # Less than two primes

        min_difference = float("inf")
        closest_pair = (-1, -1)

        for index in range(1, len(prime_numbers)):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = prime_numbers[index - 1], prime_numbers[index]

        return closest_pair