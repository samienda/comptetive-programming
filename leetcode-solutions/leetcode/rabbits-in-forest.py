class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        rabbits = defaultdict(int)
        count = 0


        for answer in answers:
            rabbits[answer] += 1

            if (rabbits[answer] - 1) % (answer + 1) == 0:
                count += answer + 1

        return count
