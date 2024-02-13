# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        count = 0

        ans = 0
        while curr.next:
            curr = curr.next
            count += 1

        curr = head
        while curr:
            if curr.val == 1:
                ans += 2 ** (count)
            count -= 1
            curr = curr.next

        return ans
