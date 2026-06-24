from typing import Optional, List


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        cur = head.next
        next = cur.next

        def critical(prev, cur, next):
            return (
                    prev.val < cur.val > next.val
                    or
                    prev.val > cur.val < next.val
            )

        min_nodes = float('inf')
        max_nodes = -1

        prev_critical_idx = 0
        first_critical_idx = 0
        i = 1  # index of cur

        while next:
            if critical(prev, cur, next):
                if first_critical_idx:
                    max_nodes = i - first_critical_idx
                    min_nodes = min(min_nodes, i - prev_critical_idx)
                else:
                    first_critical_idx = i
                prev_critical_idx = i

            prev = cur
            cur = next
            next = next.next
            i += 1

        if min_nodes == float('inf'):
            min_nodes = -1

        return [min_nodes, max_nodes]


# Time:  O(n)
# Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(5,
                ListNode(3,
                         ListNode(1,
                                  ListNode(2,
                                           ListNode(5,
                                                    ListNode(1,
                                                             ListNode(2)))))))

sn = Solution()
print(sn.nodesBetweenCriticalPoints(head))
