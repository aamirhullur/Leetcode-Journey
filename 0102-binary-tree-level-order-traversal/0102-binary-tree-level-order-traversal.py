# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []

        queue = deque([[root,0]])   
        res = defaultdict(list)
        while queue:
            curr, lvl = queue.popleft()
            if curr:
                res[lvl].append(curr.val)

                queue.append([curr.left,lvl+1])
                queue.append([curr.right,lvl+1])
        
        return(list(res.values()))
