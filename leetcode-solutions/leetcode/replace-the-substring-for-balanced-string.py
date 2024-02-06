class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)

        dic = Counter(s)

        have = Counter()
        need = Counter()

        for key, value in dic.items():
            if value > (n // 4):
                need[key] = value - (n // 4)

        if not need:
            return 0

        # print(need)
        left = 0
        count = n
        k = len(need)
        for right in range(n):
            have[s[right]] += 1

            if s[right] in need and have[s[right]] == need[s[right]]:
                k -= 1




            while k == 0:
                # if k == 0:
                    # print( s[left - 3:left], left, s[left: right + 1], right, s[right + 1: right + 4], right - left + 1)
                count = min(count, right - left + 1)


                have[s[left]] -= 1

                if s[left] in need and need[s[left]] > have[s[left]]:
                    k += 1

                left += 1


                

        return count

