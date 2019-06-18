# This program displays largest number of given Number

# Function to check largest Number
def largest(num1,num2,num3):

   if (num1>num2) and (num1>num3):
       return num1

   elif (num2>num3) and (num2>num1):
       return num2

   elif (num3>num1) and (num3>num2):
       return num3

# Main
if __name__=="__main__":
    num1=(input("Enter the 1st Number"))
    num2=(input("Enter the 2st Number"))
    num3=(input("Enter the 3st Number"))
    
    print(largest(num1,num2,num3))
