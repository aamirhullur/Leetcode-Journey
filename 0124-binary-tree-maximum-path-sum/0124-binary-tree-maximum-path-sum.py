# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = float('-inf')
        def dfs(node):
            if not node: return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            print([left_sum,right_sum,node.val])
            path = left_sum+right_sum+node.val
            self.res = max(self.res, path, node.val, right_sum+node.val ,left_sum+node.val)
            print([self.res, path, node.val, right_sum+node.val ,left_sum+node.val])
            return max(node.val+left_sum,node.val+right_sum,node.val)
            
        dfs(root)
        return(self.res)