# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        

        start = list1
        while start and a > 1:
            start = start.next    
            b -= 1
            a -= 1

        end = start
        
        while end and b >= 0:
            end = end.next
            b -= 1

        curr = list2
        while curr and curr.next:
            curr = curr.next

        start.next = list2
        curr.next = end

        return list1



        
