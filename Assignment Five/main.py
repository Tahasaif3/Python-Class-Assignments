from file_utils import ATM

atm_machine_cli = ATM()

while True:
    print("\n--- ATM Machine CLI ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
 
    if choice == 1:
        pin = int(input("Enter your account PIN to Check Balance: "))
        atm_machine_cli.check_balance(pin)

    elif choice == 2:
        pin = int(input("Enter your account PIN to Deposit Money: "))
        amount = int(input("Enter the amount to deposit into your account: "))
        atm_machine_cli.deposit(amount, pin)

    elif choice == 3:
        pin = int(input("Enter your account PIN to Withdraw Money: "))
        amount = int(input("Enter the amount to withdraw from your account: "))
        atm_machine_cli.withdraw(amount, pin)

    elif choice == 4:
        atm_machine_cli.quit()
        break

    else:
        print("Invalid choice. Try again!")

print("\nThank you for using the ATM CLI!")
