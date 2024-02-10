class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        prefix = [0] * (2051 - 1950)

        for birth, death in logs:
            prefix[birth - 1950] += 1
            prefix[death - 1950] -= 1

        mini, idx = 0, 0
        running = 0
        for i in range(2051 - 1950):
            p = prefix[i]
            running += p

            if running > mini:
                mini = running
                idx = i

        return idx + 1950

        
        