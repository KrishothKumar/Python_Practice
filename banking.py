# This program is used diposit and withdrawal

def transaction(user_input):
    print(type(user_input))
    account_balance = 0
    while True:
        if user_input[0] == "d" or user_input[0] == "D":
            account_balance += int(user_input[1::])
        elif user_input[0] =="w" or user_input[0] == "W":
            account_balance += int(user_input[1::])
        elif user_input == "end" or user_input == "END":
            break

    return account_balance



if __name__=="__main__":
    print(transaction(input("Enter The valuse for deposit D followed by Number for withdrawal W followed by Number for stop enter end:"
         )))
