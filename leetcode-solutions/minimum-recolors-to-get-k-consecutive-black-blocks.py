class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        oper = 0
        left = 0
        res = n + 1

        for right in range(n):
            if blocks[right] == 'W':
                oper += 1
            

            if right - left + 1 == k:
                res = min(res, oper)
                if blocks[left] == 'W':
                    oper -= 1
                left += 1

        return res
