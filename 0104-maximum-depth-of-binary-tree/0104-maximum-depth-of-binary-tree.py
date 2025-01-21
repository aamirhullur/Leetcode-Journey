# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        ###Recursive

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        ### Iterative        
        # if not root:
        #     return None

        # stack = [[root, 1]]
        # res = 0

        # while stack:
        #     node, num = stack.pop()
        #     res = max(res, num)
        #     if node.left:
        #         stack.append([node.left, num+1])
        #     if node.right:
        #         stack.append([node.right, num+1])

        # return res