class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()
        def pick(curr, curr_sum):
            nonlocal res
            if curr_sum > target:
                return 

            if curr_sum == target:
                curr.sort()
                res.add(tuple(curr))
                return 

            for candidate in candidates:
                pick(curr + [candidate], curr_sum + candidate)


        pick([], 0)
        return res
        