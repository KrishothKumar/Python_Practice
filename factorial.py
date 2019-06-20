# This program is to print factorial

def factorial(num):
    factor = 1

    for i in range(1,num+1,1):
        factor *= i

    return factor


# main
if __name__ == "__main__":
    nums=int(input("Enter the number for factorial: "))
    print("factorial of ",nums," is ",factorial(nums))
