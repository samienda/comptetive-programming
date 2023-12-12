class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)

        dic = defaultdict(list)
        ans = [0] * n

        for i, num in enumerate(nums):
            dic[num].append(i)

        for was, willbe in operations:

            i = dic[was][0] 
            dic.pop(was)
            dic[willbe].append(i)


   

        for i in dic:
            index = dic[i][0]
            ans[index] = i


        return ans