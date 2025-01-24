# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        arr = []

        def dfs(node,arr):
            if not node:
                return 
            dfs(node.left,arr)
            arr.append(node.val)
            dfs(node.right,arr)
        
        dfs(root,arr)

        return arr