class Solution:
    def minProcessingTime(self, p: List[int], t: List[int]) -> int:
        p.sort(reverse=True)
        t.sort()
        n = len(p)

        maxi = 0
        for i in range(n):
            item = i * 4
            task = max(t[item], t[item + 1], t[item + 2], t[item + 3])
            maxi = max(maxi, task + p[i])


        return maxi


        