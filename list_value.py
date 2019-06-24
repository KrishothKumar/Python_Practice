# This program is used to display given number in list or not

# new = []
# for i in range(0,len(list)):
#     if list[i]<= list[i+1]:
#         new.append(list[i])
#     elif list[i]>=list[i+1]:
#         new.append(list[i+1])
# print(new)
def user_list(list, use):

    list.sort()
    return use in list

# Main Statement
if __name__ == "__main__":
    list = [10,2,3]
    user_input = 12

    if user_list(list,user_input):
        print("given value is in list")
    else:
        print("given value is not in list")
