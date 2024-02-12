# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head

        while n > 0:
            fast = fast.next

            n -= 1

        slow = head
        prev = ListNode(-1)
        prev.next = slow

        count = 0
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

            count += 1

        
        prev.next = slow.next

        if count == 0:
            head = slow.next




        return head


        # print()
        