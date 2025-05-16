class ATM:
    def __init__(self):
        self.__balance = 5000
        self.__pin = 1234

    def check_pin(self,input_pin:int):
        return input_pin == self.__pin
    
    def check_balance(self,input_pin):
        if self.check_pin(input_pin):
            print(f"Your Current Balance is: {self.__balance} rupees in your account.")
        else:
            print("Invalid PIN!")

    def deposit(self,amount:int,input_pin:int):
        if not self.check_pin(input_pin):
            print("Invalid PIN!")
        elif amount > 0:
            self.__balance += amount
            print(f"You have Deposited {amount} rupees in your account.")
            print(f"Your New balance is {self.__balance} rupees")
        else:
            print("Amount must be greater than 0")

    def withdraw(self,amount:int,input_pin:int):
        if not self.check_pin(input_pin):
            print("Invalid PIN!")
        elif amount > self.__balance:
            print("Insufficient balance in your account")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.__balance -= amount
            print(f"You have Withdrawn {amount}. rupees from your account.")  
            print(f"Your New balance is {self.__balance} rupees")
    
    def quit(self):
        print("Exiting the ATM Machine CLI!")