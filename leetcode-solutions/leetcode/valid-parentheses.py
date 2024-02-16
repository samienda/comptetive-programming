class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {']': '[', ')':'(', '}':'{'}

        for ch in s:
            if ch in '[({':
                stack.append(ch)
            else:
                if not stack or stack.pop() != dic[ch]:
                    return False

        return True if not stack else False
                
