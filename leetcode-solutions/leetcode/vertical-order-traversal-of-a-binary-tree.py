# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        dic = defaultdict(list)
        def traverse(root, row, col):
            nonlocal dic
            if not root:
                return

            dic[col].append([row, root.val])

            traverse(root.left, row + 1, col - 1)
            traverse(root.right, row + 1, col + 1)

        traverse(root, 0, 0)
        res = []

        for key, value in sorted(dic.items()):

            value.sort(key=lambda item:item[1])
            value.sort()
            curr = [j for i, j in value]
            res.append(curr)


        return res
        