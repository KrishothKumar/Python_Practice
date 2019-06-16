# This program is to find whether give input is prime or not

def prime(num):
    if num == 2:
        return True
    elif num%2==0:
        return False
    for i in range(3, (num//3),2):
        if(num % i == 0):
            return False
    return True
    # if not (num%2 == 0):
    #     return 1
    # else:
    #     return 0

if __name__ == "__main__":
    # nu is reference of input Number and i is reference of prime function input
    nu=int(input("Enter the Number: "))
    i = prime(nu)

    if i:
        print("Giver Value is Prime")
    else:
        print("Given Value is Not a Prime")
