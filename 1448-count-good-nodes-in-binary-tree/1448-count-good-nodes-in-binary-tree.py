# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = [[root,root.val]]
        res = 0

        while stack:
            node, currMax = stack.pop()

            if node.val >= currMax:
                res+=1
                currMax = max(currMax,node.val)
            if node.left:
                stack.append([node.left,currMax])
            if node.right:
                stack.append([node.right,currMax])
        
        return res
                