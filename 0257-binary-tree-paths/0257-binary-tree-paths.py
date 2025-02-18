# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res = []
        def dfs(node,arr):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node.val)
                res.append("->".join(map(str, list(arr))))
                arr.pop()
                return

            arr.append(node.val)
            dfs(node.left,arr)
            dfs(node.right,arr)
            arr.pop()

        dfs(root,[])

        return res