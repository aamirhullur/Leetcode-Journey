# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        ### Recursive

        # if not root:
        #     return None
        
        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root


        ###Iterative DFS
        # if not root:
        #     return None

        # stack = [root]

        # while stack:
        #     node = stack.pop()

        #     node.left, node.right = node.right, node.left

        #     if node.left:
        #         stack.append(node.left)
            
        #     if node.right:
        #         stack.append(node.right)

        # return root

        
        ###Iterative BFS

        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


        



