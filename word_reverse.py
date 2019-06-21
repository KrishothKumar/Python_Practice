# This program is used to reverse the given word

def string_reverse(list_string):
    list_string.reverse()
    return " ".join(list_string)


# Main
if __name__ == "__main__":
    string_list="Pradeep loves swetha but she don't knows it"
    string_list=string_list.split()
    print(string_reverse(string_list))
