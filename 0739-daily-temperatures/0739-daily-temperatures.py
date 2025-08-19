class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t,index = stack.pop()
                res[index] = idx-index

            stack.append((temp,idx))
            # if not stack or temp <= stack[-1][0]:
                # stack.append((temp,idx))
        return res