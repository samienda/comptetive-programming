class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)


        first = Counter(s1)
        second = Counter(s2[:n])
        

        for right in range(n, m):
            left = right - n

            if first == second:
                return True

            second[s2[left]] -= 1
            if second[s2[left]] == 0:
                second.pop(s2[left])
            left += 1

            second[s2[right]] += 1


        return False if first != second else True