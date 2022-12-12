from to_do import TODO

class Account:
    def __init__(self, balance: float):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float):
        self.__balance += amount
        return self.__balance

    def withdrawal(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
        return self.__balance

    def fee(self):
        self.__balance *= 0.95



if __name__ == "__main__":
    # Create an account with a balance of 1000

    account = Account(balance=1000)

    # Deposit 500
    account.deposit(0)

    # Withdraw 100
    account.withdrawal(0)

    # Pay a fee
    account.fee()

    print(account.withdrawal(100))
    print(account.deposit(amount=100))




