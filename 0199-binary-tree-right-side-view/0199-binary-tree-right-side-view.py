# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [[root,0]]
        res = []
        visited = set()

        while stack:
            curr, lvl = stack.pop()
            if curr and lvl not in visited:
                visited.add(lvl)
                res.append(curr.val)
                stack.append([curr.left, lvl+1])
                stack.append([curr.right, lvl+1])
            elif curr and lvl in visited:
                stack.append([curr.left, lvl+1])
                stack.append([curr.right, lvl+1])
        
        return res



