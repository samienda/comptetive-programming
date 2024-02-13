# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head



        tail = head
        count = 0
        found = False
        while tail.next:
            tail = tail.next
            count += 1

        if count % 2 == 0:
            found = True
        hold = tail


        prev = head 
        while prev and prev.next and prev.next.next and hold != prev:
            # print('space')
            curr = prev.next

            # print(head)
            prev.next = curr.next

            curr.next = None
            if not found:
                found = True
                hold = curr

            tail.next = curr
            tail = tail.next

            prev = prev.next
        
        

        return head




        
        # while slow and slow.next and slow.next.next:
        #     slow = slow.next.next
        return head