# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        def max_depth(node):
            if not node:
                return 0
            depth_left = max_depth(node.left)
            depth_right = max_depth(node.right)
            self.res = max(self.res,depth_left+depth_right)
            return 1 + max(depth_left,depth_right)
        
        max_depth(root)
        return (self.res)