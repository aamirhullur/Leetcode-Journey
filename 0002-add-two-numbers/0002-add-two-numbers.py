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
        
        # curr1, curr2 = l1,l2

        # s1,s2 = "",""

        # while curr1 or curr2:
        #     if curr1:
        #         s1 = str(curr1.val)+s1
        #         curr1 = curr1.next
        #     if curr2:
        #         s2 = str(curr2.val)+s2
        #         curr2 = curr2.next

        # s3 = int(s1) + int(s2)
        # # print(str(s3)[::-1])
        # node = ListNode(val=None)
        # curr3= node
        # for i in str(s3)[::-1]:
        #     curr3.next = ListNode(int(i))
        #     curr3 = curr3.next
        # return node.next


        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next




