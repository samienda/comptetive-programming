class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        n = len(spaces)

        for i in range(n):
            s = s[:spaces[i] + i] + " " + s[spaces[i] + i:]



        return s
        