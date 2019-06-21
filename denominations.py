# This program is use to display the Denomination valuse


def change(user_input): # 7889 => 1889
    denomination_list = [2000,500,200,100,50,20,10,5,2,1]
    result_list = []

    for list_input in denomination_list:
        if user_input >= list_input and user_input > 0:

            reminer_value = user_input//list_input
            user_input = user_input % list_input
            result_list.append((list_input, reminer_value))

    return result_list


# Main
if __name__=="__main__":

    print(change(4300))
