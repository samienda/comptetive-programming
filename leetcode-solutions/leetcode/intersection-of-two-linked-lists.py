# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        a = headA
        b = headB



        while b:
            b.val = str(b.val)
            b = b.next

        while a:
            if type(a.val) == str:
                # a.val = int(a.val)

                b = headB
                while b:
                    b.val = int(b.val)
                    b = b.next


                return a 
            
            a = a.next
        
        b = headB
        while b:
            b.val = int(b.val)
            b = b.next

        return None
        