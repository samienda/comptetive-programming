class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        keyboard = ['qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM']
        for word in words:

            # lets find in which row do the first letter belongs to
            for buttons_row in keyboard:
                if word[0] in buttons_row:
                    row = keyboard.index(buttons_row)
                    break

        
            n = len(word)
            i = 0 # for iterating the word
            while i < n:
                if word[i] not in keyboard[row]:
                    break

                i += 1    
            else:
                result.append(word)

        return result