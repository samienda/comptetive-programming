# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """"
        [-10,-3,0,5,9]
                    -10,-3          0,          5,9
                    -10                         5
                none    -3                 none     9

        """

        def divide(left, right):
            if left > right:
                return 


            mid = (left + right) // 2
            left = divide(left, mid - 1)
            right = divide(mid + 1, right)

            return TreeNode(nums[mid], left, right)

        return divide(0, len(nums) - 1)
