class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [ (i, num) for i, num  in enumerate(nums)]

        def merge(lefthalf, righthalf):
            left = 0
            right = 0
            newlis = []
            count = 0
            # print(memo)
            while left < len(lefthalf) and right < len(righthalf):
                if lefthalf[left][1] > righthalf[right][1]:
                    count += 1
                    newlis.append(righthalf[right])
                    right += 1
                else:
                    memo[lefthalf[left][0]] += count
                    newlis.append(lefthalf[left])
                    left += 1

            while left < len(lefthalf):
                memo[lefthalf[left][0]] += count
                newlis.append(lefthalf[left])
                left += 1

            while right < len(righthalf):
                newlis.append(righthalf[right])
                right += 1

            return newlis


        def divide(left, right, nums):
            if left == right:
                return [nums[left]]

            mid = (left + right) // 2
            
            return merge(divide(left, mid, nums), divide(mid + 1, right, nums))

        memo = defaultdict(int)
        divide(0, n - 1, nums)

        ans = [0] * n
        for idx, value in memo.items():
            ans[idx] = memo[idx]
        # print(memo)
        return ans
            

        