# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        first = list1
        second = list2


        merged = ListNode()
        head = merged

        while first and second:
            if first.val < second.val:
                merged.next = ListNode(first.val)
                first = first.next
            else:
                merged.next = ListNode(second.val)
                second = second.next
                
            merged = merged.next

        
        while first:
            merged.next = ListNode(first.val)
            first = first.next
            merged = merged.next
        
        while second:
            merged.next = ListNode(second.val)
            second = second.next
            merged = merged.next

        return head.next