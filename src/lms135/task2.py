from to_do import TODO

class Account:
    def __init__(self, balance: float):
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float):
        self.__balance += amount

    def withdrawal(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount

    def fee(self):
        self.__balance *= 0.95


if __name__ == "__main__":

