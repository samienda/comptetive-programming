# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head

        while curr:
            if curr.val == 's':
                return True
            
            curr.val = 's'
            curr = curr.next

        
        return False
        