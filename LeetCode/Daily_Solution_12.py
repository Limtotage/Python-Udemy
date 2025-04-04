# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Daily_Solution_12:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
            if slow==fast:
                return True
        return False
