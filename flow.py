from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(Fore.GREEN + f"✔ KES {amount} deposited successfully.")
        else:
            print(Fore.RED + "✘ Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(Fore.GREEN + f"✔ KES {amount} withdrawn successfully.")
            else:
                print(Fore.RED + "✘ Insufficient balance.")
        else:
            print(Fore.RED + "✘ Invalid withdrawal amount. Please enter a positive number.")

    def check_balance(self):
        print(Fore.YELLOW + f"💰 Your current balance is: KES {self.balance}")

def display_menu():
    print(Fore.CYAN + "\n======== MAIN MENU ========")
    print(Fore.CYAN + "1. 🆕 Create Account")
    print(Fore.CYAN + "2. 💵 Deposit")
    print(Fore.CYAN + "3. 💳 Withdraw")
    print(Fore.CYAN + "4. 📊 Check Balance")
    print(Fore.CYAN + "5. 🚪 Exit")
    print(Fore.CYAN + "============================")

def main():
    print(Fore.MAGENTA + "Welcome to the ATM!")
    
    account = None
    
    while True:
        display_menu()
        
        choice = input(Fore.CYAN + "Enter your choice: ")

        if choice == '1':
            if account is None:
                print(Fore.LIGHTGREEN_EX + "\n--- Create Account ---")
                name = input(Fore.LIGHTWHITE_EX + "Please enter your name: ")
                try:
                    initial_balance = float(input(Fore.LIGHTWHITE_EX + "Please enter your initial balance: "))
                    if initial_balance < 0:
                        print(Fore.RED + "✘ Initial balance cannot be negative.")
                    else:
                        account = Account(name, initial_balance)
                        print(Fore.GREEN + "✔ Account created successfully!")
                except ValueError:
                    print(Fore.RED + "✘ Invalid balance input. Please enter a numeric value.")
            else:
                print(Fore.YELLOW + "⚠ An account already exists.")

        elif choice == '2':
            if account:
                print(Fore.LIGHTGREEN_EX + "\n--- Deposit Money ---")
                try:
                    deposit_amount = float(input(Fore.LIGHTWHITE_EX + "Enter deposit amount: "))
                    account.deposit(deposit_amount)
                except ValueError:
                    print(Fore.RED + "✘ Invalid amount. Please enter a numeric value.")
            else:
                print(Fore.RED + "✘ No account found. Please create an account first.")

        elif choice == '3':
            if account:
                print(Fore.LIGHTGREEN_EX + "\n--- Withdraw Money ---")
                try:
                    withdrawal_amount = float(input(Fore.LIGHTWHITE_EX + "Enter withdrawal amount: "))
                    account.withdraw(withdrawal_amount)
                except ValueError:
                    print(Fore.RED + "✘ Invalid amount. Please enter a numeric value.")
            else:
                print(Fore.RED + "✘ No account found. Please create an account first.")

        elif choice == '4':
            if account:
                print(Fore.LIGHTGREEN_EX + "\n--- Check Balance ---")
                account.check_balance()
            else:
                print(Fore.RED + "✘ No account found. Please create an account first.")

        elif choice == '5':
            print(Fore.LIGHTMAGENTA_EX + "\nThank you for using Python ATM. Goodbye!")
            break

        else:
            print(Fore.RED + "✘ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
