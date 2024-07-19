# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def traverse(node):
            nonlocal count
            if node and  not node.left and not node.right:return [1]

            if not node:
                return []

            left = traverse(node.left)
            right = traverse(node.right)

            new_lis = []
            for numleft in left:
                for numright in right:
                    if numleft + numright <= distance:
                        count += 1

            for num in right:
                if num < distance:
                    new_lis.append(num + 1)

            for num in left:
                if num < distance:
                    new_lis.append(num + 1)

            return new_lis

        count = 0
        traverse(root)
        return count