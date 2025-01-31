class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # res = []

        # for l in range(len(temperatures)):
        #     r = l
        #     while r < len(temperatures) and temperatures[r] <= temperatures[l]:
        #         r+=1
        #     if r < len(temperatures):
        #         res.append(r-l)
        #     else:
        #         res.append(0)

        # return(res)

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                m,n = stack.pop()
                res[n] = i - n
            
            stack.append([temperatures[i],i])
        return res