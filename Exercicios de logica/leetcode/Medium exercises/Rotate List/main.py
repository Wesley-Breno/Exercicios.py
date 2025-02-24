from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1. Determine the size of the list and find the last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Adjust k to avoid unnecessary rotations
        k = k % length
        if k == 0:
            return head

        # 3. Find the new end of the list (the node before the new head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # 4. Rearrange the pointers to form the new list
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head  # Connect the old last node to the old head

        return new_head
