class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,r in enumerate(temperatures):
            while stack and r > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([r,i])
        return res