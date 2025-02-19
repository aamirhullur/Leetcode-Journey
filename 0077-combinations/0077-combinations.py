class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        # res = []

        # def bt(i,currArr):
        #     if len(currArr) == k:
        #         res.append(list(currArr))
        #         return
        #     if i > n:
        #         return
 
        #     currArr.append(i)
        #     bt(i+1,currArr)

        #     currArr.pop()
        #     bt(i+1,currArr)

        # bt(1,[])

        # return res


        res = []

        def bt(i,currArr):
            if i > n:
                return
            elif len(currArr) == k:
                res.append(list(currArr))
            else:
                for j in range(i+1,n+1):
                    currArr.append(j)
                    bt(j,currArr)
                    currArr.pop()

        bt(0,[])

        return res