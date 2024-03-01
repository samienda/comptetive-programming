class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def pick(curr, have, n):
            nonlocal res
            if have < 0 or have > n:
                return 
            if n == 0:
                if have == 0:
                    res.append(curr)
                return 

            pick(curr + '(', have + 1, n - 1)
            pick(curr + ')', have - 1, n - 1)

        pick("", 0, 2 * n)
        return res