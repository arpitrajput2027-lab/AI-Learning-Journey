class BankAccount:
    def __init__(self, account_holder,account_number, balance):
        self.account_holder = account_holder    # Public attribute
        self._account_number = account_number  # Protected attribute
        self.__balance = balance        # Private attribute
    
acc1 = BankAccount("Arpit", "1234567890", 5000000000)
print("Account Holder :", acc1.account_holder)  # Accessing Public Attribute

print("Account Number :", acc1._account_number)  # Accessing Protected Attribute (not recommended)
# print("Balance :", acc1.__balance)  # Accessing Private Attribute (will raise AttributeError) but
print("Balance :", acc1._BankAccount__balance)


    