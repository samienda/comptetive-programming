class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        high = sum(w)
        # print(high)

        res = []
        def divide(low, high):
            nonlocal res
            if low > high:
                return 

            curr = 0
            maxload = (low + high) // 2
          
            currday = 1

            maximum = 0
            for num in w:
                if maxload < num:
                    currday = days + 1
                    break

                if curr + num > maxload:     
                    currday += 1
                    maximum = max(maximum, curr)
                    curr = num
                else:
                    curr += num


            maximum = max(maximum, curr)
            if days >= currday:
                res.append(maximum)
                high = maxload - 1
            else:
                low = maxload + 1

            divide(low, high)

        divide(w[0], high)
        # print(res)
        return min(res)

        

                
