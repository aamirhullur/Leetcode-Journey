class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {}

        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        last = self.tail.prev

        last.next = node
        self.tail.prev = node

        node.prev = last
        node.next = self.tail
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            oldNode = self.nodeMap[key]
            self._remove(oldNode)
        
        newNode = ListNode(key,value)
        self._add(newNode)
        self.nodeMap[key] = newNode

        if len(self.nodeMap) > self.capacity:
            node_to_remove = self.head.next
            self._remove(node_to_remove)
            self.nodeMap.pop(node_to_remove.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)