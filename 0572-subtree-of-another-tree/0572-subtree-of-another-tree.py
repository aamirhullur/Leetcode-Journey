# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        # def inorder(node,arr):
        #     if not node:
        #         return
            
        #     inorder(node.left,arr)
        #     arr.append(node.val)
        #     inorder(node.right,arr)

        #     return arr

        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            elif root.val != subRoot.val:
                return False
            
            return isSameTree(root.left,subRoot.left) and isSameTree(root.right,subRoot.right)

        stack = [[root, subRoot]]
        
        while stack:

            root, subRoot = stack.pop()
            if root and subRoot:
                if root.val == subRoot.val:
                    print([root.val,subRoot.val])
                    # arr1, arr2 = [], []
                    # t1 = inorder(root,arr1)
                    # t2 = inorder(subRoot,arr2)
                    # print([t1,t2])
                    # if t1 == t2:
                    #     return True
                    res = isSameTree(root,subRoot)
                    if res:
                        return True
                stack.append([root.left, subRoot])
                stack.append([root.right, subRoot])
            else:
                continue
        
        return False