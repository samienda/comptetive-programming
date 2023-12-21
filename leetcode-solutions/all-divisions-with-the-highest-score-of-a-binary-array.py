class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score = Counter(nums)
        ds = defaultdict(list)
        n = len(nums)
        score[0] = 0 

        ds[score[0] + score[1]].append(0)
        for i in range(1, n + 1):
            num = nums[i - 1]
            if num == 0:
                score[num] += 1
            else:
                score[num] -= 1

            ds[score[0] + score[1]].append(i)

        return ds[max(ds)]
