# This program is use to Chnage the String from uppercase to lowercase, lowercase to uppercase and camelcase to lower or uppercase

def lowercase(string):
    for i in range(0,len(string)):
        if (ord(string[i])>=65) and (ord(string[i])<=90):

            string = string[:i]+ chr(ord(string[i])+32)+string[i+1:]

    return string

def uppercase(string):
    for i in range(0,len(string)):
        if (ord(string[i])>=97) and (ord(string[i])<=122):

            string = string[:i]+ chr(ord(string[i])-32)+string[i+1:]

    return string

def camelcase(string):
    for i in range(0,len(string)):
        if (ord(string[i])== 32):
            if (ord(string[i+1])>=97) and (ord(string[i+1])<=122):
                string = string[:i+1]+ chr(ord(string[i+1])-32)+string[i+2:]

    string = string.split()
    string = "".join(string)
    return string

# Main statement
if __name__ == "__main__":
    string = input("Enter the string :")
    print(lowercase(string))
    print(uppercase(string))
    print(camelcase(string))
