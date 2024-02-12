# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        fast = head
        slow = head

        while fast:
            fast = fast.next

            if n % 2 == 0:
                slow = slow.next

            n += 1
        return slow
        # print(slow.val)
        # n //= 2

        # middle = head
        # while n > 0:
        #     middle = middle.next

        #     n -= 1

        # return middle

        