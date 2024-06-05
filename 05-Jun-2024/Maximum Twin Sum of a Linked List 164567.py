# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lis = []

        while head:
            lis.append(head.val)
            head = head.next

        maxi = 0
        for i in range(len(lis)//2):
            maxi = max(maxi, lis[i] + lis[-(i + 1)])

        return maxi