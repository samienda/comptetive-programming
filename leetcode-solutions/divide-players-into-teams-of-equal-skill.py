class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()

        left = 0
        right = n - 1
        curr = 0

        while left < right:
            if skill[left + 1] - skill[left] == skill[right] - skill[right - 1]:
                curr += (skill[left] * skill[right])
            else:
                return -1

            left += 1
            right -= 1


        return curr  

        