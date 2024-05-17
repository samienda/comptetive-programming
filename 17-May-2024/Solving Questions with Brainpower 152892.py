# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def solve(idx):
            if idx >= len(questions):
                return 0

            
            return max(
                solve(idx + 1),
                solve(idx + questions[idx][-1] + 1) + questions[idx][0]
            )

        return solve(0)