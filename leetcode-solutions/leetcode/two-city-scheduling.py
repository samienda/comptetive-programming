class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        def compare(items):
            return (items[0] - items[1])

        costs.sort(key=compare)

        total = 0
        # i = a = b = 0
        # while i < n: 
        #     if costs[i][0] > costs[i][1]:
        #         a += 1
        #         total += costs[i][1]
        #     else:
        #         b += 1
        #         total += costs[i][0]

        #     i += 1
        #     if abs(a - b) > n - i - 1:
        #         while a > b:
        #             total += costs[i][0]
        #             b += 1
        #             i += 1

        #         while b > a:
        #             a += 1
        #             total += costs[i][1]
        #             i +=1


        for i in range(n//2):
            total += costs[i][0]
            total += costs[n - i - 1][1]

        return total


        

        return total
                

