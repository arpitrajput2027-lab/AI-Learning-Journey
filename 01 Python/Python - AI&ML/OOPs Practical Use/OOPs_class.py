class SbiBankAtm:

    def __init__(self):
        self.pincode = ""
        self.balance = 0

    def run(self):
        while True:
            user_input = input(""" 
Hello Sir/Mam , How would You like to Proceed :
1.) Enter 1 to registering your Pincode
2.) Enter 2 to Deposit
3.) Enter 3 to Withdraw
4.) Enter 4 to Check Balance
5.) Enter 5 to Exit
""")
            if user_input == "1":
                self.register_pincode()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw_amount()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Bye")
                break
            else:
                print("Invalid choice, please enter 1-5.")

    def register_pincode(self):
        self.pincode = input("Enter Your Pincode : ")
        print("Pincode Registered Successfully")

    def deposit(self):
        if not self.pincode:
            print("Please register your pincode first.")
            return
        temp = input("Enter Your PIN: ")
        if self.pincode == temp:
            amount = int(input("Enter the Amount to be Deposit: "))
            self.balance += amount
            print(f"{amount} deposited. Available balance: {self.balance}")
        else:
            print("Invalid Pin, Please Try Again.")

    def withdraw_amount(self):
        if not self.pincode:
            print("Please register your pincode first.")
            return
        temp = input("Enter Your PIN: ")
        if self.pincode == temp:
            amount = int(input("Enter the Amount You Want to Withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn from your account, available balance is {self.balance}")
            else:
                print("You have not sufficient amount in your account to withdraw")
        else:
            print("Invalid Pin, Please Try Again")

    def check_balance(self):
        if not self.pincode:
            print("Please register your pincode first.")
            return
        temp = input("Enter Your PIN: ")
        if self.pincode == temp:
            print(f"Available Balance: {self.balance}")
        else:
            print("Invalid Pin, Please Try Again")


if __name__ == "__main__":
    atm = SbiBankAtm()
    atm.run()