class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)


        left = 0
        dic = Counter()
        longest = 0
        for right in range(n):

            while s[right] in dic:
                dic.pop(s[left])
                left += 1

            longest = max(longest, right - left + 1)
            dic[s[right]] += 1

        return longest

