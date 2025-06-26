# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node,d):
            if not node:
                return
            
            if len(res)==d:
                res.append(node.val)
            
            dfs(node.right,d+1)
            dfs(node.left,d+1)


        dfs(root,0)
        return res

