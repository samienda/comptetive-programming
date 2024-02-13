# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Buble sort
        
        slow = head
        was = slow.val
        curr = head
        while curr:
            slow = head
            fast = slow.next

            while fast :
                if slow.val > fast.val:
                    slow.val, fast.val = fast.val, slow.val
                fast = fast.next
                slow = slow.next

            curr = curr.next
        return head
