class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)


        right = set()
        wrong = set()

        for i in range(n):
            if backs[i] != fronts[i]:
                right.add(backs[i])
                right.add(fronts[i])
            else:
                wrong.add(backs[i])



        ans = right - wrong
        mini = float('inf')

        for num in ans:
            mini = min(mini, num)

        return mini if mini != float('inf') else 0




        


        