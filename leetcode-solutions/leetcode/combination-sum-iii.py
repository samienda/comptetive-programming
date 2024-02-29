class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        maximum = (9 * (1 + 9)) // 2

        if n  > maximum:
            return []

        res = []
        def pick(curr, summ, num):
            nonlocal res
            if len(curr) >= k:
                if summ == n:
                    res.append(curr)
                return 
                
            if num > 9:
                return 

            pick(curr + [num], summ + num,  num + 1)
            pick(curr, summ,  num + 1)
            
        pick([], 0, 1)

        return res
        