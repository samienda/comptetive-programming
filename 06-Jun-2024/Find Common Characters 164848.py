# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        target = Counter(words[0])

        for word in words:
            count = Counter(word)

            for i in target:
                if count[i] < target[i]:
                    target[i] = count[i]

        answer = []
        for i in target:
            for _ in range(target[i]):
                answer.append(i)

        return answer