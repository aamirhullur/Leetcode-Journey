# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import base64
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.maxD = 0
        def dfs(node,d):
            if not node:
                return
            self.maxD=max(self.maxD,d)
            dfs(node.left,d+1)
            dfs(node.right,d+1)

        dfs(root,1)
        return self.maxD