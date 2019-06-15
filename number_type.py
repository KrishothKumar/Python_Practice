# This program is to find whether give input is prime or not

def prime(num):
    if not(num%2 == 0):
        print("Prime",num)
    else:
        print("Even",num)

if __name__ == "__main__":
    print(prime(4))
