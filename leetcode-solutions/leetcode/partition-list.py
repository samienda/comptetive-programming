# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        flag = True


        less = ListNode()
        dummyless = less
        greater = ListNode()
        dummygreater = greater

        curr = head

        while curr:
            temp = curr.next
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr.next = None
            curr = temp

        less.next = dummygreater.next
        # greater.next = None
        # print(less)


        return dummyless.next
                