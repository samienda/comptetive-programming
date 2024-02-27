class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def pick(curr, idx):
            nonlocal res
            if idx > n:
                if len(curr) == k:
                    res.append(curr)
                return 

            pick(curr + [idx], idx + 1)
            pick(curr, idx + 1)
        
        pick([], 1)
        return res