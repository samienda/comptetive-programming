# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        curr = node
        prev = ListNode()
        prev.next = curr
        
        while curr and curr.next:
            prev = curr
            curr = curr.next

            prev.val, curr.val = curr.val, prev.val


        prev.next = None


        