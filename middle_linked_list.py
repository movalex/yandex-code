from typing import Any, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        "[{}]".format(", ".join(map(str, self)))


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        n = 0

        while cur:
            n += 1
            cur = cur.next
        cur = head
        n = (n // 2) + 1
        i = 0

        while cur:
            i += 1
            if i == n:
                head = cur
                return head
            cur = cur.next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle: Optional[ListNode] = head
        end: Optional[ListNode] = head

        while end and end.next:
            middle = middle.next
            end = end.next.next
        return middle
