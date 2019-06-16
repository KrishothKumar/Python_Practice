#This program

def nex_prime(num):
    if num ==0 or num ==1:
        num=1
    for i in range(num+1, (num+1)*2, 1):
        if prime(i):
             return i

def prime(num):
    if num == 2:
        return True
    elif num%2==0:
        return False
    elif num == 1:
        return False

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
