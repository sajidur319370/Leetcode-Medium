from typing import Optional


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        head = reverse(head)
        cur = head
        cur_max = cur.val
        while cur and cur.next:
            if cur.next.val < cur_max:
                cur.next = cur.next.next
            else:
                cur_max = cur.next.val
                cur = cur.next

        return reverse(head)


# Time:O(n)
# Space:O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

sn = Solution()
print(sn.removeNodes(head))
