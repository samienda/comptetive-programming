class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        queue = deque(senate)


        r = 0
        d = 0

        while queue and r < n and d < n:
            if queue[0] == 'R':
                if d == 0:
                    queue.append(queue.popleft())
                    r += 1
                else:
                    queue.popleft()
                    d -= 1
            else:
                if r == 0:
                    queue.append(queue.popleft())
                    d += 1
                else:
                    queue.popleft()
                    r -= 1
        # print(r, d)
        return 'Radiant' if r > d else 'Dire'