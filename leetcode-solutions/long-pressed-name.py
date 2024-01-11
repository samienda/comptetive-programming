class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        n = len(name)
        m = len(typed)
        right = 0
        left = 0



        while left < n and right < m:

            if name[left] == typed[right]:
                left += 1
                right += 1
            else:
                if name[left - 1] != typed[right]: # check if it is longpressed or wrong character
                    return False
                right += 1


        # if the first and the last characters must be the same
        if name[0] != typed[0]:
            return False


        while right < m:
            if name[n - 1] != typed[right]:
                return False
            right += 1


        return left == n 



        

        