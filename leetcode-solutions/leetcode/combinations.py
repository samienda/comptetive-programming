class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def pick(curr, idx):
            nonlocal res
            if len(curr) > k:
                return 
                
            if idx > n or len(curr) == k:
                if len(curr) == k:
                    res.append(curr)
                return 

            pick(curr + [idx], idx + 1)
            pick(curr, idx + 1)
        
        pick([], 1)
        return res