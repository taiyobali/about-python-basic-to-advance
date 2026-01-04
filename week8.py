# simple and beginner-friendly project
# Basic Banking System
from func import *
accounts = []

def main():
    is_running = True
    while is_running:
        print("__________User___________")
        print("1. Create new account.")
        print("2. Delete Account.")
        print("3. Update Account PIN.")
        print("4. Deposit Money.")
        print("5. Withdraw Money.")
        print("6. Show Info.")
        print("7. Exit.")
        print("___________________________")
        user = input("Choose an option(1-7): ").strip()
        match user:
            case "1":
                add_acc()
            case "2":
                user = int(input("Enter User ID: "))
                delete_acc(user)
            case "3":
                user = int(input("Enter User ID: "))
                old = int(input("Enter previous pin: "))
                new = int(input("Enter new pin(4-digits):"))
                update_pin(user,old,new)
            case "4":
                user = int(input("Enter User ID: "))
                amount = float(input("Enter amount for deposit: "))
                deposit(user,amount)
            case "5":
                user = int(input("Enter User ID: "))
                pin = int(input("Enter pin: "))
                amount = float(input("Enter amount for deposit: "))
                withdraw(user,pin,amount)
            case "6":
                user = int(input("Enter User ID: "))
                show(user)
            case "7":
                is_running = False
            case _:
                print("please, input an valid number(1-7).")
                continue
if __name__ == "__main__":
    main()























