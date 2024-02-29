class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        total = sum(candidates) 
        unique = set(candidates)
        if total < target:
            return []

        if total == target:
            return [candidates]


        candidates.sort()
        res = set()
        final = False
        def pick(curr, summ, idx):
            nonlocal res, final, unique
            if summ >= target:
                if summ == target:
                    if sum(unique) <= target and len(res) == len(unique):
                        final = True
                    res.add(tuple(sorted(curr)))
                return 

            if idx >= len(candidates):
                return 

            if not final:   
                pick(curr + (candidates[idx],), summ + candidates[idx], idx + 1)
                pick(curr, summ, idx + 1)

        pick(tuple(), 0, 0)
        return res
        