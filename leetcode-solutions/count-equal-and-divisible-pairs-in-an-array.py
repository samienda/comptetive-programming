class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        n = len(nums)

        for i in range(n):
            dic[nums[i]].append(i)


        count = 0
        print(dic)
        for key in dic:
            value = dic[key]
            m = len(value)

            if m >1:
                
                for i in range(m- 1):
                    for j in range(i + 1, m):
                        print(value[i], value[j])
                        if (value[i] * value[j]) % k == 0:
                            count += 1


        return count
        