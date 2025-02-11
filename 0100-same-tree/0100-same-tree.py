# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        
        stack = [[p,q]]
        tmp = True
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if node1 and node2:
                print([node1.val,node2.val])
                if node1.val != node2.val:
                    tmp = False
                stack.append([node1.left,node2.left])
                stack.append([node1.right,node2.right])
            else:
                tmp = False
            
        return tmp