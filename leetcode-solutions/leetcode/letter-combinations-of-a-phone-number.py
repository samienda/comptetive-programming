class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        memo = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []

        def pick(curr, idx):
            nonlocal res, memo
            if idx >= len(digits):
                if curr:
                    res.append("".join(curr))
                return 


            print(curr)
            for ch in memo[digits[idx]]:
                pick(curr + [ch], idx + 1)

        pick([], 0)

        return res


        