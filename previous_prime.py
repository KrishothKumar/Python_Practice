
def previous_prime(num):
    for i in range( num-1 , 1 , -1 ):
        if prime(i):
            return i


def prime(num):
    if num == 2:
        return True
    elif num%2 == 0:
        return False

    for i in range(3, (num//3),2):
        if(num % i == 0):
            return False

    return True


# mani
if __name__ == "__main__":
    num= int(input("Enter the Number: "))

    i = previous_prime(num)
    print("If givien Number is",num," and the previous Prime Number is",i)
