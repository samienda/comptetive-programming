# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        answer = []
        def pick(idx, curr):
            if idx >= len(s):
                answer.append(curr)
                return

            if s[idx].isdigit():
                pick(idx + 1, curr + s[idx])
            else:
                pick(idx + 1, curr + s[idx].upper())
                pick(idx + 1, curr + s[idx].lower())

        pick(0, "")
        return answer