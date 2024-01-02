class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        mini = min(costs)
        maxi = max(costs)

        counts = [0] * (maxi + 1)

        for cost in costs:
            counts[cost] += 1

        res = 0
        res_count = 0
        for i in range(maxi  + 1):
            for _ in range(counts[i]):
                res += i
                res_count += 1

                if res > coins:
                    return res_count - 1



        return res_count