class RecentCounter:

    def __init__(self):
        self.recent = []
        self.pointer = 0
        

    def ping(self, t: int) -> int:
        self.recent.append(t)

        while self.recent[self.pointer] < t - 3000:
            self.pointer += 1
        return len(self.recent[self.pointer:])
        
        # return len(self.recent)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)