class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        memo = {}
        for i in range(n):
            memo[i] = (i + nums[i]) % n
        # print(memo)
        dic = memo.items()
        

        haveseen = set()
        for i in range(n):
            if i in haveseen:
                continue
            left = i
            count = 0
            seen = set()
            last =  float('inf')
            while  count < n:
                # print(last, left)
                if nums[left] > 0 and nums[i] < 0:
                    break

                if nums[left] < 0 and nums[i] > 0:
                    break
                

                seen.add(left)
                haveseen.add(left)
                last =  left
                left = memo[left]

                if  left == last:
                    print("same")
                    break
                if left in seen:
                    return True
                count += 1

        return False




        