# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(lefthalf,righthalf):

            left = lefthalf
            right = righthalf

            newnode = ListNode()
            starting = newnode

            while left and right:
                if left.val > right.val:
                    newnode.next = ListNode(right.val)
                    right = right.next
                else:
                    newnode.next = ListNode(left.val)
                    left = left.next

                newnode = newnode.next

            while left:
                newnode.next = ListNode(left.val)
                left = left.next
                newnode = newnode.next

            while right:
                newnode.next = ListNode(right.val)
                right = right.next
                newnode = newnode.next

            return starting.next

        k = len(lists)
        def combine(left, right, lists):
            # print(left, right)
            if left == right:
                return lists[left]

            mid = (left + right) // 2

            lefthalf = combine(left, mid, lists)
            righthalf = combine(mid + 1, right, lists)

            return merge(lefthalf, righthalf)

        return combine(0, k - 1, lists) if lists else None





