class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)


        left = 0
        dic = Counter()
        length = n + 1

        for right in range(n):
            dic[cards[right]] += 1

            if dic[cards[right]] == 2:
                while cards[left] != cards[right]:
                    dic[cards[left]] -= 1
                    left += 1

                length = min(length, right - left + 1)
                dic[cards[left]] -= 1
                left += 1
        

        return length if length != n + 1 else -1


                
