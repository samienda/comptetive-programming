# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(left, right):

            newnode = ListNode()
            starting = newnode

            while left and right:
                if left.val > right.val:
                    newnode.next = ListNode(right.val)
                    right  = right.next
                else:
                    newnode.next = ListNode(left.val)
                    left  = left.next

                newnode = newnode.next

            while left:
                newnode.next = left
                left  = left.next
                newnode = newnode.next

            while right:
                newnode.next = right
                right  = right.next
                newnode = newnode.next

            return starting.next


        def divide(head):
            if not head or not head.next: return head

            fast = head
            slow = head
            mid = slow

            while slow and fast and fast.next:
                mid = slow
                slow = slow.next
                fast = fast.next.next

            mid.next = None
            # print(head, mid,slow)
            left = divide(head)
            right = divide(slow)

            return merge(left, right)

        return divide(head)



            






            



        