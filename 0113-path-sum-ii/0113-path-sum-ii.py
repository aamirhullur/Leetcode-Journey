# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import *

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        arr = []
        res = []
        def bt(node, currSum, arr,res):
            if not node: return
            if not node.left and not node.right:
                currSum += node.val
                arr.append(node.val)
                if currSum == targetSum:
                    res.append(list(arr))
                currSum -= node.val
                arr.pop()
                return
            
            currSum += node.val
            arr.append(node.val)

            bt(node.left, currSum, arr, res)
            bt(node.right,currSum,arr,res)
            arr.pop()
        
        bt(root, 0, arr, res)
        return res

