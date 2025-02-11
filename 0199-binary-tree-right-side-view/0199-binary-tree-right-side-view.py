# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        visited = set()
        stack = [[root,0]]
        res = []
        while stack:
            print(visited)
            node,dep = stack.pop()

            if node and dep not in visited:
                visited.add(dep)
                res.append(node.val)
                stack.append([node.left,dep+1])
                stack.append([node.right,dep+1])
            elif node and dep in visited:
                stack.append([node.left,dep+1])
                stack.append([node.right,dep+1])
        
        return res

