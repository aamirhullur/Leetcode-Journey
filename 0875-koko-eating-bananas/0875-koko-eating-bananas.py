class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        res = r

        def calc(val):
            tmp = 0
            for i in piles:
                tmp += int(math.ceil(float(i)/val))
            return tmp

        while l <= r:
            m = (l + r)//2
            val = calc(m)
            if val <= h:
                res = m
                r = m-1
            else:
                l = m+1
        return res
