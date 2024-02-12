# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        n = 0

        curr = head

        while curr:
            curr = curr.next

            n += 1

        n = (n // 2)

        middle = head
        while n > 0:
            middle = middle.next

            n -= 1

        return middle

        