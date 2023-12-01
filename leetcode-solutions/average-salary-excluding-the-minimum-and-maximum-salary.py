class Solution:
    def average(self, salary: List[int]) -> float:
        minim = min(salary)
        maxim = max(salary)

        return (sum(salary) - minim - maxim) / (len(salary)- 2)