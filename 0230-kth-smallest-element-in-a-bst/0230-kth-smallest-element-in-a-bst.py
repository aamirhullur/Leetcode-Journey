# Definition for a binary tree node.
class TreeNode:
    def __init__(self,val=0,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        self.arr = 0
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            self.cnt -= 1
            if not self.cnt:
                self.arr = node.val
                return
            dfs(node.right)

        dfs(root)

        return self.arr