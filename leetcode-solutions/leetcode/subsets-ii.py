class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()
        def pick(curr, idx):
            nonlocal res
            # print(curr)
            if idx >= len(nums):
                res.add(curr)
                return
            
            pick(curr + (nums[idx],), idx + 1)
            
            pick(curr, idx + 1)
        
        pick(tuple(), 0)
        
        return res