# This program is used diposit and withdrawal and show full account_balance

def transaction(methodToRun):
    account_balance = 0

    while True:
        user_inputs =  methodToRun()

        if user_inputs[0] == "d" or user_inputs[0] == "D":
            account_balance += int(user_inputs[1::])

        elif user_inputs[0] =="w" or user_inputs[0] == "W":
            account_balance -= int(user_inputs[1::])

        elif user_inputs == "end" or user_inputs == "END":
            break

    return account_balance

def user_input():
    valus=input("Enter The valuse for deposit D followed by Number \nfor withdrawal W followed by Number for stop enter end:\n")
    return valus

# Main
if __name__=="__main__":
    value1 = transaction(user_input)
    print ("Know account balance is", value1)
