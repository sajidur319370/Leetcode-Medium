from typing import Optional, List


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        base = length // k
        reminder = length % k
        parts = []

        curr = head
        for i in range(k):
            part_size = base + (1 if i < reminder else 0)
            if part_size == 0:
                parts.append(None)
                continue

            part_head = curr
            parts.append(part_head)

            for j in range(part_size - 1):
                curr = curr.next

            next_part = curr.next
            curr.next = None
            curr = next_part

        return parts



# Time Complexity: O(n)
# Space Complexity: O(k)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next.next = ListNode(10)

sn = Solution()
print(sn.splitListToParts(head, 3))
