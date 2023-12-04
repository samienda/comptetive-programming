class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        n = len(ghosts)

        res = []
        x, y = target
        steps = abs(x) + abs(y)

        for g in ghosts:
            h, k = g

            res.append(abs(x - h) + abs(y - k))

        mini = min(res)

        return True if steps < mini else False 

        