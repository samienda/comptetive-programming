# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = defaultdict(list)
        depth = 0

        def zigzag(root):
            nonlocal depth, res
            if not root:
                return

            res[depth].append(root.val)
            depth += 1
            zigzag(root.left)
            zigzag(root.right)
            depth -= 1

        ans = []
        zigzag(root)
        for i, elem in res.items():
            if i % 2 == 0:
                ans.append(elem)
            else:
                ans.append(reversed(elem))

        return ans

