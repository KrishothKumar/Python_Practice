# This program is used to find the give string is palindrome or not

def palindrome(str):
    return str == str[::-1]

# Main
if __name__ == "__main__":
    x=palindrome("mom")

    if x:
        print("is palindrome")
    else:
        print("is not palindrome")
