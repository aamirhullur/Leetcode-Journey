# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.right and not root.left:
                return None
            elif not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            curr = root.left
            while curr.right:
                curr = curr.right
            
            root.val = curr.val
            root.left = self.deleteNode(root.left,curr.val)
        
        return root
        