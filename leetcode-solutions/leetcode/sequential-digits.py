class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # 12345
        # 23456
        # 34567
        # 45678
        # 56789

        # 1 9
        # 2 8
        # 3 7
        # 4 6
        # 5 5
        # 6 4
        # 7 3
        # 8 2
        # 9 1

        l = len(str(low))
        h = len(str(high))
        res = []
        nums = '123456789'

        for i in range(l, h + 1):
            add = int('1' * i)
            curr = int(nums[:i])

            for _ in range(10 - i):
                if low <= curr <= high:
                    res.append(curr)
                
                curr += add

        return res