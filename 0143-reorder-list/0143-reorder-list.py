# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # curr = head
        # arr = []

        # while curr:
        #     arr.append(curr)
        #     curr = curr.next
        
        # l,r = 0, len(arr)-1
        
        # while l<r:
        #     # if l == r:
        #     #     # arr2.append(arr[l])
        #     #     arr[l].next = arr[r]
        #         # break
        #     arr[l].next = arr[r]
        #     l+=1
        #     arr[r].next = arr[l]
        #     r-=1
        
        # arr[l].next = None
        

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        curr = head

        while curr:
            tmp1 = curr.next
            curr.next = prev
            curr = tmp1
            if curr == prev:
                break
            tmp2 = prev.next
            prev.next = curr
            prev = tmp2
    