class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def pick(curr, idx):
            nonlocal res
            if idx >= len(nums):
                res.append(curr)
                return 

            pick(curr + [nums[idx]], idx + 1)
            pick(curr, idx + 1)

        pick([], 0)
        return res
        