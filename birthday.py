# This program is used to view birthday date based on name

def birthday_date(user_name,birthday_dictionary):# Input as Name and Dictionary
    dummy_list = []

    for new_data in birthday_dictionary["birthday"]: # It take each data and validate the name in Dictionary
        if new_data["Name"] == user_name:
            dummy_list.append((new_data["DOB"],new_data["ID"]))
        else:
            break
    return dummy_list

#Main statement
if __name__=="__main__":
    # Dictionary Data
    birthday_dictionary = {
    "birthday":
    [
    {
    "ID": 120,
    "Name": "Krishoth",
    "DOB": "16-3-1996"
    },
    {
    "ID": 121,
    "Name": "Krishoth",
    "DOB": "4-11-1996"
    },
    {
    "ID": 122,
    "Name": "Pradeep",
    "DOB": "28-5-1994"
    }
    ]
    }

    user_name = input("Enter the name to se the date of bith: ")
    final_data = birthday_date(user_name,birthday_dictionary)

    if final_data == []:
        print("No data found")

    else:
        for i in final_data:

            print("Given Name is",user_name,"and Date of birth ",i[0]," and ID No", i[1])

    # for i in x['birthday']:
    #     print("%s: %d" % (i, x[i]))
