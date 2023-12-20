class ATM:

    def __init__(self):
        self.dic = {0:0, 1:0, 2:0, 3:0, 4:0}
        self.money = [20, 50, 100, 200, 500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, dep in enumerate(banknotesCount):
            self.dic[i] += dep
        

    def withdraw(self, amount: int) -> List[int]:
        print(self.dic)
        cash = 0
        i = 4
        res = [0] * 5
        self.temp = self.dic.copy()
        while i >= 0:
            if self.dic[i] != 0:
                res[i] += amount // self.money[i]
                amount %= self.money[i]
                if self.dic[i] < res[i]:
                    diff = res[i] - self.dic[i]
                    amount += (diff * self.money[i])
                    res[i] = self.dic[i]
            i -= 1

        
        if amount == 0:
            for i in range(5):
                self.dic[i] -= res[i]
            print(self.dic)
            return res
        else:
            print(self.dic)
            return [-1]    

            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)