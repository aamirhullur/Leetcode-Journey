# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        curr1, curr2 = l1,l2

        s1,s2 = "",""

        while curr1 or curr2:
            if curr1:
                s1 = str(curr1.val)+s1
                curr1 = curr1.next
            if curr2:
                s2 = str(curr2.val)+s2
                curr2 = curr2.next

        s3 = int(s1) + int(s2)
        # print(str(s3)[::-1])
        node = ListNode(val=None)
        curr3= node
        for i in str(s3)[::-1]:
            curr3.next = ListNode(int(i))
            curr3 = curr3.next
        return node.next




