class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = []

        def bt(i,currArr):
            if len(currArr) == k:
                print(currArr)
                res.append(list(currArr))
                return

            if i > n:
                return
 

            currArr.append(i)
            bt(i+1,currArr)

            currArr.pop()
            bt(i+1,currArr)

        bt(1,[])

        return res