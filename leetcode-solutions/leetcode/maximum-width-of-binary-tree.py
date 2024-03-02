# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dicleft = defaultdict(list)
        dicright = defaultdict(list)

        def inorderleft(root, row, col):
            nonlocal dicleft
            if not root:
                return root

            dicleft[row].append(col)

            inorderleft(root.left, row + 1, 2 * col)
            inorderleft(root.right, row + 1, 2 * col - 1)

        def inorderright(root, row, col):
            nonlocal dicright
            if not root:
                return root

            dicright[row].append(col)

            inorderright(root.left, row + 1, 2 * col - 1)
            inorderright(root.right, row + 1, 2 * col)

        inorderleft(root.left, 1, 1)
        inorderright(root.right, 1, 1)
        max_ = 0

        # print(dicleft)
        # print(dicright)

        for key, value in dicleft.items():
            if dicright[key]:
                max_ = max(max_, max(value) + max(dicright[key]))
            if len(value) > 1:
                max_ = max(max_, max(value) - min(value) + 1)
            if len(dicright[key]) > 1:
                max_ = max(max_, max(dicright[key]) - min(dicright[key]) + 1)

        for key, value in dicright.items():
            if key not in dicleft and len(value) > 1:                
                max_ = max(max_, max(value) - min(value) + 1)
                
            

        if not max_ and root:
            return 1


        return max_ 