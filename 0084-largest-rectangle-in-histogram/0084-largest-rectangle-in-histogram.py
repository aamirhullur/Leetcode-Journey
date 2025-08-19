class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        res = 0
        stack = []

        for idx,height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                index = stack.pop()
                h = heights[index]
                w = idx - stack[-1] - 1
                res = max(res,w*h)
            stack.append(idx)

        return res