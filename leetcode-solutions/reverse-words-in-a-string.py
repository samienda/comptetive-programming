class Solution:
    def reverseWords(self, s: str) -> str:

        string = list(s.split())
        n = len(string)
        ans = ""

        for s in string:
            ans = s + " " + ans


        return ans.strip()

        