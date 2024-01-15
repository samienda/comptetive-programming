class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        leftF= leftT = 0
        kF = kT = k


        for right in range(n):
            if answerKey[right] == 'T':
                kF -= 1
            else:
                kT -= 1

            if kT < 0:
                if answerKey[leftT] == 'F':
                    kT += 1
                leftT += 1

                
            if kF < 0:
                if answerKey[leftF] == 'T':
                    kF += 1
                leftF += 1


        return max(right - leftT, right - leftF) + 1




