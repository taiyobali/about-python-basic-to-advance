from week8 import accounts
def add_acc():
    name = input("Enter your name: ").strip().title()
    id_num = int(input("Enter account ID (5-digits): "))
    pin = int(input("Enter PIN(4-digits): "))
    dept = float(input("Initial Deposit Money: $"))
    accounts.append({"user": name,
                     "user_id": id_num,
                     "pin": pin,
                     "balance": dept
                     })


def delete_acc(user_id):
    if not accounts:
        return print("No data Available")
    found = False
    for index, user in enumerate(accounts):
        if user.get("user_id") == user_id:
            found = True
            accounts.pop(index)
            print(f"{user_id} deleted.")
    if not found:
        print(f"{user_id} is not found!")


def update_pin(user_id: int, old_pin: int, new_pin: int):
    if not accounts:
        return print("No data Available")
    found = False
    for index, user in enumerate(accounts):
        if user.get("user_id") == user_id:
            found = True
            if accounts[index].get("pin") == old_pin:
                accounts[index].update({"pin": new_pin})
                print(f"{user_id} pin updated.")
            else:
                print("It's wrong pin.")
    if not found:
        print(f"{user_id} is not found!")

def deposit(user_id:int,amount):
    if not accounts:
        return print("No data Available")
    found = False
    for index, user in enumerate(accounts):
        if user.get("user_id") == user_id:
            found = True
            if amount>=0:
                accounts[index]["balance"] += amount
                print(f"{user_id} balance deposited.")
            else:
                print("Insufficient funds")
    if not found:
        print(f"{user_id} is not found!")

def withdraw(user_id,pin,amount):
    if not accounts:
        return print("No data Available")
    found = False
    for index, user in enumerate(accounts):
        if user.get("user_id") == user_id:
            found = True
            if amount>=0:
                if accounts[index]["balance"]>=amount:
                    if accounts[index]["pin"] == pin:
                        accounts[index]["balance"] -= amount
                        print(f"{user_id} balance withdraw successful.")
                    else:
                        print("invalid pin")
                else:
                    print("insufficient funds")
            else:
                print("Amount must be grater than zero.")
    if not found:
        print(f"{user_id} is not found!")

def show(user_id):
    if not accounts:
        return print("No data Available")
    found = False
    for index, user in enumerate(accounts):
        if user.get("user_id") == user_id:
            found = True
            import pandas as pd
            df = pd.DataFrame([user])
            print(df)
    if not found:
        print(f"{user_id} is not found!")


