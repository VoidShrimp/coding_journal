def main():
    balance = 50.00

    print("*******************************")
    print("Banking Program")
    print("*******************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("*******************************")
    run = True
    while run:
        print("Enter your choice (1-4): ")
        user_choice = int(input())
        if user_choice == 1:
            show_balance(balance)
        elif user_choice == 2:
            print("How much would you like to deposit today? $")
            user_deposit = float(input())
            balance = deposit(user_deposit, balance)
        elif user_choice == 3:
            print("How much would you like to withdraw today? $")
            user_withdraw = float(input())
            balance = withdraw(user_withdraw, balance)
        elif user_choice == 4:
            run = False
        else:
            print("Invalid option")
            run = True

def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")

def deposit(user_deposit, balance):
    new_balance = user_deposit + balance
    print(f"Your balance is: ${new_balance:.2f}")
    return new_balance

def withdraw(user_withdraw, balance):
    new_balance = balance - user_withdraw
    print(f"Your balance is: ${new_balance:.2f}")
    return new_balance

main()