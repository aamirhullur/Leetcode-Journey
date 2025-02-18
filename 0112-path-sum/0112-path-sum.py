# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def bt(node,currSum):
            if not node:
                return False

            
            currSum += node.val

            if not node.left and not node.right:
                if currSum == targetSum:
                    return True
                else:
                    currSum -= node.val
                    return False

            return bt(node.left,currSum) or bt(node.right,currSum)
        
        return bt(root,0)



