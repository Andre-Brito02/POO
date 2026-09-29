class BankAccount:
    def __init__(self, number_account:int, name:str, initial_value=0.0):
        self._number_account = number_account
        self._name = name
        self._balance = initial_value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        self._name = name

    def deposit(self, deposit_value:float):
        if deposit_value > 0:
            self._balance += deposit_value

    def withdraw(self, withdraw_value:float):
        if withdraw_value > 0:
            self._balance -= (withdraw_value + 5.0)

    def __str__(self):
        return f"Account {self._number_account}, Holder: {self._name}, Balance: $ {self._balance:.2f}"

number_account = int(input("Enter account number: "))
name = input("Enter account holder: ").title()
choice = input("Is there an initial deposit? ")

if choice.lower() == 'y':
    initial_value = float(input("Enter initial deposit value: "))
    ba = BankAccount(number_account, name, initial_value)
else:
    ba = BankAccount(number_account, name)

print('\nAccount data: ')
print(ba, "\n")

deposit_value = float(input("\nEnter a deposit value: "))
ba.deposit(deposit_value)
print('\nUpdated account data: ')
print(ba, "\n")

withdraw_value = float(input("\nEnter a withdraw value: "))
ba.withdraw(withdraw_value)
print('\nUpdated account data: ')
print(ba, "\n")