# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        # arr = []

        # def post(root):
        #     if not root:
        #         return 

        #     post(root.left)
        #     post(root.right)
        #     arr.append(root.val)
        
        # post(root)

        # return arr


        arr = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                arr.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left

        arr.reverse()
        return arr

