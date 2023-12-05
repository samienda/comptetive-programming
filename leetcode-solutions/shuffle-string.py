class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        result = [''] * n

        for i in range(n):
            character = s[i]
            idx = indices[i]

            result[idx] = character

        output = ""
        for res in result:
            output += res

        return output