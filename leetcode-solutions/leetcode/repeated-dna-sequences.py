class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)


        left = 0
        curr = ''
        count = Counter()

        if n < 10:
            return []


        for right in range(9, n):
            curr = s[left:right + 1]

            count[curr] += 1

            left += 1

        res = []
        for key, value in count.items():
            if value > 1:
                res.append(key)


        return res

        


        