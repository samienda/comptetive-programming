# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # elem = []
        curr = head

        back = None
        
        while curr:
            # elem.append(curr.val)
            newnode = ListNode(curr.val)
            curr = curr.next
            newnode.next = back
            back = newnode

        # print(back)
        # print(head)

        curr = head
        while curr:
            if curr.val != back.val:
                return False
            curr = curr.next
            back = back.next

    


        return True

        