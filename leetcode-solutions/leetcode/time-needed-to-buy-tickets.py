class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]

        tickets = [[i, t] for i, t in enumerate(tickets)]

        queue = deque(tickets)

        time = 0
        while target:
            left = queue.popleft()
            left[1] -= 1
            time += 1

            if left[1]:
                queue.append(left)
            else:
                if k == left[0]:
                    break

        return time


            




        