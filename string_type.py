# This program is use to Chnage the String from uppercase to lowercase, lowercase to uppercase and camelcase to lower or uppercase

def lowercase(string):
    for i in range(0,len(string)):
        if (ord(string[i])>=65) and (ord(string[i])<=90):

            string =string[:i]+ chr(ord(string[i])+32)+string[i+1:]

    return string

def uppercase(string):
    for i in range(0,len(string)):
        if (ord(string[i])>=97) and (ord(string[i])<=122):

            string =string[:i]+ chr(ord(string[i])-32)+string[i+1:]

    return string

def camelcase(string):
    pass



# Main statement
if __name__ == "__main__":
    str = "KrishZ"
    print(str[5:])
    print(chr(0))
    print(chr(1))
    print(chr(2))
    print(chr(3))
    print(chr(4))
    print(lowercase(str))
