class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        need = Counter(s)
        have = Counter()
        n = len(s)


        k = 0
        left = 0
        res = []

        for i in range(n):
            have[s[i]] += 1

            if have[s[i]] == need[s[i]]:
                k += 1

            if k == len(have):
                res.append(i - left + 1)
                left = i + 1

        return res



        