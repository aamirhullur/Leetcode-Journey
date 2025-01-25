# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.tmp = True
        def find_len(node):
            if not node:
                return 0

            left = find_len(node.left)
            right = find_len(node.right)
            
            if abs(left-right) > 1:
                self.tmp = False
            
            return 1 + max(left,right)
            
        
        find_len(root)
        return self.tmp