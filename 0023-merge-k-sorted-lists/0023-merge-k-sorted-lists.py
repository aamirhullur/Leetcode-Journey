# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self,l1,l2):
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            newList = []

            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None

                newList.append(self.merge(list1,list2))
            lists = newList
        return lists[0]
