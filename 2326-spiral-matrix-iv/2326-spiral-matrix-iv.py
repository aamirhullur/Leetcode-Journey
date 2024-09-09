# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        grid = [[-1] * n for i in range(m)]
        cur = head
        flag = 1
        i, j= 0,-1
        while cur:
            for _ in range(n):
                if cur:
                    j+=flag
                    grid[i][j] = cur.val
                    cur = cur.next
            m-=1
            for _ in range(m):
                if cur:
                    i+=flag
                    grid[i][j] = cur.val
                    cur = cur.next
            n -= 1
            flag *= -1
        return grid