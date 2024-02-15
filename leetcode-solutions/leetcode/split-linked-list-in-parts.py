# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        curr = head
        n = 0

        while curr:
            curr = curr.next
            n += 1
        

        rem = n % k
        size = n // k

        curr = head

        res = []
        while curr:

            count = 0
            prev = ListNode()
            prev.next = curr
            temp = curr
            if rem > 0:
                count -= 1
                rem -= 1
            while count < size:
                prev = curr
                curr = curr.next
                count += 1

            prev.next = None
            res.append(temp)


            k -= 1

        while k > 0:
            res.append(None)
            k -= 1

        return res




