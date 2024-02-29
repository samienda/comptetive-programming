# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def convert(node):
            # print(node)
            if not node:
                return None

            if not node.next:
                return TreeNode(node.val)

            slow = node
            fast = node
            mid = node

            while slow and fast and fast.next:
                mid = slow
                slow = slow.next
                fast = fast.next.next

            mid.next = None
            # print(node)
            left = convert(node)
            right = convert(slow.next)

            return TreeNode(slow.val, left, right)

        return convert(head)
        