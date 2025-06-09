# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return -1
        p = deque(preorder)

        lookup = {v:i for i,v in enumerate(inorder)}
        def rec(start,end):
            if start > end:
                return None
            else:
                cand = p.popleft()
                root = TreeNode(cand)
                mid = lookup[cand]
                root.left = rec(start, mid-1)
                root.right = rec(mid+1, end)
                return root

        return rec(0,len(preorder)-1)
