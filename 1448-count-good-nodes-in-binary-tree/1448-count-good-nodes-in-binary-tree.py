# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [[root,float('-inf')]]
        res = 0
        while stack:
            node, max_val = stack.pop()

            if node:
                print([node.val,max_val,res])
                # res += 1 if node.val >= max_val else 0
                if node.val >= max_val:
                    max_val = node.val
                    res += 1
                stack.append([node.left,max_val])
                stack.append([node.right,max_val])
        
        return res
