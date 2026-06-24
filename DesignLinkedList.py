class ListNode:
    def __init__(self, val=0,prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr!= self.tail and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        new_node.next = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            new_node = ListNode(val)
            curr.prev.next = new_node
            new_node.prev = curr.prev
            curr.prev = new_node
            new_node.next = curr


    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr!= self.tail and index == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            del curr



obj = MyLinkedList()

obj.addAtHead(1)     # list: 1
obj.addAtTail(3)     # list: 1 -> 3
obj.addAtIndex(1, 2) # list: 1 -> 2 -> 3

print(obj.get(1))    # ?
obj.deleteAtIndex(1) # list: 1 -> 3

print(obj.get(1))    # ?