# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = Counter()
        def traverse(root):        
            nonlocal dic
            if not root:
                return

            dic[root.val] += 1

            traverse(root.left)
            traverse(root.right)

        traverse(root)
        # print(dic)

        res = []
        last = -1
        for key, value in sorted(dic.items(), key=lambda item:item[1], reverse=True):
            if last != -1 and value != last:
                break
            res.append(key)
            last = value

        return res
