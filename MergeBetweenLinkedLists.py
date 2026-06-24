# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        i = 0

        while i < a - 1:
            head = head.next
            i += 1

        tail = head

        while i <= b:
            tail = tail.next
            i += 1

        head.next = list2
        cur = list2

        while cur.next:
            cur = cur.next

        cur.next = tail

        return list1


# Time:O(N)
# Space:O(1)


# List1
list1 = ListNode(10)
list1.next = ListNode(20)
list1.next.next = ListNode(30)
list1.next.next.next = ListNode(40)
list1.next.next.next.next = ListNode(50)
list1.next.next.next.next.next = ListNode(60)
list1.next.next.next.next.next.next = ListNode(70)
list1.next.next.next.next.next.next.next = ListNode(80)

# List2
list2 = ListNode(5)
list2.next = ListNode(15)
list2.next.next = ListNode(25)
list2.next.next.next = ListNode(35)
list2.next.next.next.next = ListNode(45)
list2.next.next.next.next.next = ListNode(55)
list2.next.next.next.next.next.next = ListNode(65)
list2.next.next.next.next.next.next.next = ListNode(75)
list2.next.next.next.next.next.next.next.next = ListNode(85)
list2.next.next.next.next.next.next.next.next.next = ListNode(95)

sn = Solution()
print(sn.mergeInBetween(list1=list1, a=2, b=4, list2=list2))
