# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        stack = []

        curr = head
        idx = 0
        memo = {}
        while curr:
            while stack and stack[-1][0] < curr.val:
                value, i = stack.pop()
                memo[i] = curr.val

            stack.append([curr.val, idx])
            curr = curr.next
            idx += 1

        while stack:
            value, i = stack.pop()
            memo[i] = 0

        ans = []
        for key, value in sorted(memo.items()):
            ans.append(value)

        return ans 

        