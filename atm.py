class ATM:
    def __init__(self, initial_balance=50000, default_pin="0000"):
        self.balance = initial_balance
        self.pin = default_pin

    def check_balance(self):
        print(f"\nYour current balance is: {self.balance:.2f} SDG")

    def withdraw(self, amount):
        if amount <= 0:
            return "Please enter a valid amount to withdraw."
        elif amount > self.balance:
            return "Insufficient funds. Unable to process the withdrawal."
        else:
            self.balance -= amount
            return f"Withdrawal successful! Your new balance is ${self.balance:.2f}"

    def deposit(self, amount):
        if amount <= 0:
            return "Please enter a valid deposit amount."
        else:
            self.balance += amount
            return f"Deposit successful! Your new balance is {self.balance:.2f} SDG"

    def verify_pin(self, input_pin):
        return input_pin == self.pin

    def change_pin(self, old_pin, new_pin, confirm_pin):
        if old_pin != self.pin:
            return "Incorrect current PIN."
        elif new_pin != confirm_pin:
            return "The new PIN entries do not match."
        elif len(new_pin) < 4:
            return "PIN should be at least 4 digits long."
        else:
            self.pin = new_pin
            return "PIN changed successfully."

def atm_menu():
    atm = ATM()
    print("Welcome to the ATM simulation!")
    
    # Request PIN verification at the start
    for attempt in range(3):
        input_pin = input("Please enter your PIN to access your account: ")
        if atm.verify_pin(input_pin):
            print("PIN verified. Access granted.\n")
            break
        else:
            print("Incorrect PIN. Please try again.")
    else:
        print("Too many failed attempts. Exiting.")
        return

    while True:
        print("\nPlease select an option:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                print(atm.withdraw(amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to deposit: "))
                print(atm.deposit(amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "4":
            old_pin = input("Enter current PIN: ")
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            print(atm.change_pin(old_pin, new_pin, confirm_pin))
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")

atm_menu()
