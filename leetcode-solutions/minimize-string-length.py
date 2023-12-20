class Solution:
    def minimizedStringLength(self, s: str) -> int:
        dic = defaultdict(list)
        n = len(s)
        count = 0

        for i in range(n):
            if len(dic[s[i]]) > 0:
                dic[s[i]].pop(0)
                count += 1

            dic[s[i]].append(i)


        return n - count