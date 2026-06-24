from typing import Optional


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        dummy = ListNode()
        tail = dummy

        while cur.next:

            node = ListNode()

            while cur.next.val != 0:
                node.val += cur.next.val
                cur = cur.next

            tail.next = node
            tail = tail.next
            cur = cur.next

        return dummy.next


# Time:O(n)
# Space:O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(0,
                ListNode(3,
                         ListNode(1,
                                  ListNode(0,
                                           ListNode(4,
                                                    ListNode(5,
                                                             ListNode(2,
                                                                      ListNode(0))))))))
sn = Solution()
print(sn.mergeNodes(head))
