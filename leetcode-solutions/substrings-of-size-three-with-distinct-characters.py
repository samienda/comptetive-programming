class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)


        left = 0
        count = 0
        dic = Counter(s[:2])


        for right in range(2,n):
            dic[s[right]] += 1

            if len(dic) == 3:
                count += 1

            dic[s[left]] -= 1
            if dic[s[left]] == 0:
                dic.pop(s[left])
            left += 1

        return count
             
        