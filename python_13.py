class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.get_balance())


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.04):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print("Interest Added:", round(interest, 2))


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.get_balance() + self.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            new_balance = self.get_balance() - amount
            self._BankAccount__balance = new_balance
            print("Withdrawal successful.")


# Demonstration
print("SAVINGS ACCOUNT")
savings = SavingsAccount("Vikash", 5000)
savings.deposit(1000)
savings.add_interest()
savings.display_details()

print("\nCURRENT ACCOUNT")
current = CurrentAccount("Aman", 3000, 1000)
current.withdraw(3500)
current.display_details()
