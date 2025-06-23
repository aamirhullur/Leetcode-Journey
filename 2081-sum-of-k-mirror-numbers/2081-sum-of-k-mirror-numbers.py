class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        def find_base_k(num):
            base_k = []
            while num:
                base_k.append(num%k)
                num //= k

            return base_k == base_k[::-1]


        l = 1
        res = []
        while len(res) < n:
            r = l * 10
            for p in [1, 0]:
                for i in range(l,r):
                    if len(res) == n: break

                    cpy = str(i)
                    if p == 0: cpy = cpy + cpy[::-1]
                    else: cpy = cpy[:-1] + cpy[::-1]
                    cpy = int(cpy)

                    if find_base_k(cpy):
                        res.append(cpy)
            l = r
            
        return sum(res)
        