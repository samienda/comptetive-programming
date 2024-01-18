class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        left_sum = sum(cardPoints[:k])
        right_sum = sum(cardPoints[n - k:])

        right = n - 1
        left = 0
        points = 0

        while k > 0:
            if left_sum > right_sum:
                value = cardPoints[left]
                points += value
                left += 1
                left_sum -= value
                right_sum -= cardPoints[right - k + 1]
            else:
                value = cardPoints[right]
                points += value
                right -= 1
                right_sum -= value
                left_sum -= cardPoints[left + k - 1]

            k -= 1


        return points

        

