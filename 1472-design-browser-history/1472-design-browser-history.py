class ListNode:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head, self.tail = ListNode(None),ListNode(None)
        node = ListNode(homepage)
        self.head.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = self.head
        self.curr = node

    def visit(self, url: str) -> None:
        new_node = ListNode(url,self.tail,self.curr)
        self.curr.next = new_node
        self.curr = new_node

    def back(self, steps: int) -> str:
        while steps > 0:            
            if self.curr.prev == self.head:
                return self.curr.val
            else:
                self.curr = self.curr.prev
                steps-=1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.curr.next == self.tail:
                return self.curr.val
            else:
                self.curr = self.curr.next
                steps-=1
        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)