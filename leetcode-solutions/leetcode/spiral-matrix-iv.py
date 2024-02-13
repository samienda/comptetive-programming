# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1] * n  for _ in range(m) ]
        i, j = 0, 0
        curr = head
        mat[0][0] = curr.val
        curr = curr.next

        for _ in range(n//2 + 1):

            # right 0, 1
            while curr and j + 1 < n and mat[i][j + 1] == -1:
                j += 1
                mat[i][j] = curr.val
                curr = curr.next


            # down 1 0
            while curr and i + 1 < m and mat[i + 1][j] == -1:
                i += 1
                mat[i][j] = curr.val
                curr = curr.next


            # left 0 -1
            while curr and j - 1 >= 0 and mat[i][j - 1] == -1:
                j -= 1
                mat[i][j] = curr.val
                curr = curr.next


            # up -1 0
            while curr and i - 1 >= 0 and mat[i - 1][j] == -1:
                i -= 1
                mat[i][j] = curr.val
                curr = curr.next

            # print(i, j)

        # print(mat)
        return mat
        