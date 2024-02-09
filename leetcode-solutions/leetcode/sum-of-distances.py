class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # arr = []
        
        prefix_freq = defaultdict(list)
        prefix = [0] * n

        for i in range(n):
            prefix_freq[nums[i]].append(i)

        
        for key, values in prefix_freq.items():

            prefix = [0]
            running = 0
            for value in values:
                running += value
                prefix.append(running)

            # prefix.append(prefix[len(values)])
            # print(key)
            # print(values)
            # print(prefix)

            for i in range(len(values)):
                ai = values[i]

                ans = ( ((i + 1) * (ai)) - prefix[i] )  +  ( prefix[len(values)] - prefix[i + 1] ) - ( (len(values) - i) * ai )
                # print(( ((i + 1) * (ai)) - prefix[i] ), ( prefix[len(values)] - prefix[i + 1] ), ( (len(values) - i) * ai ))

                # print(f"(({(i + 1) * (ai)}) - {prefix[i]})  + (({prefix[len(values)]} - {prefix[i + 1]}) - {((len(values) - i) * ai)})")
                # print(ans)
                nums[ai] = ans 


        # for i in range(n):
        #     score = 0

        #     for j in freq[nums[i]]:
        #         score += abs(i - j)

        #     arr.append(score)


        return nums

        