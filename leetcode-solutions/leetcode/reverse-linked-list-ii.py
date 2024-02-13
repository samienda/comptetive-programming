# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1

        if left == right:
            return head
        curr = head

        prev = ListNode()
        prev.next = curr

        dummy = None

        # find left
        while curr and  count != left:
            prev = curr
            curr = curr.next
            count += 1

        # print(curr.val)
        start = prev
        end = curr
        # reverse til we find right 
        prev = None
        temp = curr.next
        curr.next = prev
        
        while temp and count != right:
            # print(prev)
            # print(curr)
            # print(prev)
            prev = curr
            curr = temp
            temp = temp.next
            # print(prev)
            curr.next = prev
            # print(curr)
            # print(temp)
            count += 1




        start.next = curr
        end.next = temp

        return start.next if left == 1 else head

        