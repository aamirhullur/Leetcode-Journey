# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current = head

        if head is None or k < 2:
            return head
        
        for i in range(k - 1):
            current = current.next
            if current is None:
                return head

        new_list  = None
        current = head
        
        for i in range(k):
            next_node  = current.next
            current.next = new_list 
            new_list  = current
            current = next_node 
        
        head.next = self.reverseKGroup(current, k)
        return new_list 