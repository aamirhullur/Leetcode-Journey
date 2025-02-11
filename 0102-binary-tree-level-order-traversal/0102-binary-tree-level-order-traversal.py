# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        queue = deque([[root,0]])
        res = defaultdict(list)
        while queue:
            node,dep = queue.popleft()
            if node:
                res[dep].append(node.val)
                queue.append([node.left,dep+1])
                queue.append([node.right,dep+1])

        return res.values()