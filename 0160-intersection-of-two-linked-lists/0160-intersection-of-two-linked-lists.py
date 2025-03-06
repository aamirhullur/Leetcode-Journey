# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hmap = {}

        curr1, curr2 = headA, headB
        while curr1:
            hmap[curr1] = curr1.next
            curr1 = curr1.next 

        while curr2:
            if curr2 in hmap:
                return curr2
            curr2 = curr2.next

        # print(hmap.keys())