class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.sto = balance
        self.count = len(self.sto)

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1 - 1 >= self.count or account2 - 1 >= self.count: return False
        if self.sto[account1 - 1] < money: return False
        else:
            self.sto[account1 - 1] -= money
            self.sto[account2 - 1] += money
            return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account - 1 >= self.count: return False
        else: 
            self.sto[account - 1] += money
            return True
        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account - 1 >= self.count: return False
        elif self.sto[account - 1] < money: return False
        else: 
            self.sto[account - 1] -= money
            return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
