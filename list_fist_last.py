# This program is use print first and last element from list

def first_last_element(user_input):
    user_input.sort()
    return user_input[0], user_input[len(user_input)-1]


# Main Statement
if __name__ =="__main__":

    # User_list = [4,8,10,11,2,3,1]
    user_list = [int(input("Enter 1 element")),int(input("Enter 2 element")),int(input("Enter 3 element")),
                 int(input("Enter 4 element")),int(input("Enter 5 element")),int(input("Enter 6 element")),
                 int(input("Enter 7 element")),int(input("Enter 8 element")),int(input("Enter 9 element")),
                 int(input("Enter 10 element"))]
    print(first_last_element(user_list))
