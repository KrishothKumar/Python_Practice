# This program

def largest(num1,num2,num3):
   if num1<num2:
       return num2
   elif num1<num3:
       return num3
   elif num3<num1:
       return num1

#main
if __name__=="__main__":
    num1=(input("Enter the 1st Number"))
    num2=(input("Enter the 2st Number"))
    num3=(input("Enter the 3st Number"))
    print(largest(num1,num2,num3))
