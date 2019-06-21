# This program is used to display largest number from list

def largest_list(list):
    list_value = len(list)
    largest_value=0

    for each_list in range(0,list_value,1):
        if largest_value<=list[each_list]:
            largest_value=list[each_list]

    return largest_value


# Main
if __name__ =="__main__":
    lists = [5,11,2,3,6,4,7,8,10,9,1]
    print("The largest Number is the given list is ",largest_list(lists))
