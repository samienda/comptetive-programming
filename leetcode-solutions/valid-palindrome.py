class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = s.upper()
        alpha = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
)       
        letters = [letter for letter in letters if letter in alpha]
        n = len(letters)

        left = 0
        right = n - 1

        while left < right:
            if letters[left] != letters[right]:
                return False

            left += 1
            right -= 1
        
        print(letters)
        return True


