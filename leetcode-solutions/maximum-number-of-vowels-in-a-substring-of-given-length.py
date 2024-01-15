class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)


        vowels = set(['a', 'e', 'i', 'o', 'u'])
        left = 0

        num_of_vowels = 0
        max_num_of_vowels = 0


        for right in range(n):
            if s[right] in vowels:
                num_of_vowels += 1

            max_num_of_vowels = max(max_num_of_vowels, num_of_vowels)

            if right - left + 1 == k:
                if s[left] in vowels:
                    num_of_vowels -= 1
                left += 1

            


        return max_num_of_vowels
