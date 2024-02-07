class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s) + 1
        prefix = [0] * n



        for start, end, dxn in shifts:
            if dxn == 0:
                dxn = -1


            prefix[start] += dxn
            prefix[end + 1] -= dxn


        curr = 0
        for x in range(n - 1):
            curr += prefix[x]
            prefix[x] = curr


        res = ""
        for i in range(n - 1):
            value = prefix[i] + ord(s[i]) - ord('a')
            value %= 26

            res += chr(value + ord('a'))


        return res

        