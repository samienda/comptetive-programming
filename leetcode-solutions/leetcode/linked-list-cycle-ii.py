# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head

        while fast and fast.next and slow:

            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                curr = head
                while curr:
                    if curr == slow:
                        # print(curr.val, curr)
                        return curr

                    curr = curr.next
                    slow = slow.next

                # return slow

        return None

        