class ListNode:
    def __init__(self, val, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index>0:
            curr=curr.next
            index-=1
        if index == 0 and curr and curr != self.tail:
            return curr.val
        return -1


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        tmp = self.head.next 
        self.head.next = new_node
        tmp.prev = new_node
        new_node.next = tmp
        new_node.prev = self.head

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        tmp = self.tail.prev
        tmp.next = new_node
        self.tail.prev = new_node
        new_node.next = self.tail
        new_node.prev = tmp

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next

        while curr != self.tail and index > 0:
            curr = curr.next
            index -= 1
        if index == 0 and curr :
            new_node = ListNode(val)
            tmp = curr.prev 
            tmp.next = new_node
            curr.prev = new_node
            new_node.next = curr
            new_node.prev = tmp


    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next

        while curr and index>0:
            curr = curr.next
            index-=1
        if index == 0 and curr and curr != self.tail:
            L, R = curr.prev, curr.next
            L.next = R
            R.prev = L

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)