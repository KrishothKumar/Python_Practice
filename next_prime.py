#This program

def nex_prime(num):
     for i in range(num+1, num*2, 1):
         if prime(i):
             return i

def prime(num):
    if num == 2:
        return True

    for i in range(3, (num//3),2):
        if(num % i == 0):
            return False

    return True


# main
if __name__ == "__main__":
    #input Number
    num= int(input("Enter the Number: "))

    i = nex_prime(num)
    print("If givien Number is",num," and the next Prime Number is",i)
