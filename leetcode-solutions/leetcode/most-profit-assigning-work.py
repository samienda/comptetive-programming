class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)

        worker.sort()
        comb = zip(profit, difficulty)
        comb = list(comb)
        comb.sort()

        profits = 0
        workptr, diffptr = m - 1, n - 1
        while workptr > -1  and diffptr > -1:

            if worker[workptr] >= comb[diffptr][1]:
                workptr -= 1
                profits += comb[diffptr][0]
            else:
                diffptr -= 1

        return profits