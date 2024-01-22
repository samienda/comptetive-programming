class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        tree = Counter()

        left = 0
        count = 0


        for right in range(n):
            tree[fruits[right]] += 1

            while len(tree) > 2:
                tree[fruits[left]] -= 1
                if tree[fruits[left]] == 0:
                    tree.pop(fruits[left])
                left += 1

            
            count = max(count, right - left + 1)

        return count



        