class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        one = 0
        two = 0
        n = 0

        def find(left, right):
            if left == right:
                return [left, 1, 1]

            lefttotal = nums[left] + nums[right - 1] 
            righttotal = nums[right] + nums[left + 1]

            if right - left + 1 > 5:
                lefttotal += nums[left + 2]
                righttotal += nums[right - 2]

            if right - left + 1 > 7:
                lefttotal += nums[right - 3]
                righttotal += nums[left + 3]


            if right - left + 1 > 9:
                lefttotal += nums[left + 4]
                righttotal += nums[right - 4]


            if right - left + 1 > 11:
                lefttotal += nums[right - 5]
                righttotal += nums[left + 5]



            if lefttotal == righttotal:
                if nums[left] > nums[right]:
                    return [left, 1, 0]

            if lefttotal > righttotal:
                return [left, 1, 0]
            return [right, 0, 1]

        left = 0
        right = len(nums) - 1
        while left <= right:
            if n % 2 == 0:
                ans = find(left, right)
                left += ans[1]
                right -= ans[2]
                one += nums[ans[0]]
            else:
                ans = find(left, right)
                left += ans[1]
                right -= ans[2]
                two += nums[ans[0]]
            # print(one, two)
            n += 1

        return one >= two

        
        