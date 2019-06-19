#This program is used to find sum of list odd and even


def sums(num):
    sum1=0
    sum2=0

    for i in num:
        if(i%2==0):
            sum1+=i
        else:
            sum2+=i
            
    return sum1,sum2

#main
if __name__ == "__main__":
    lists = [0,1,2,3,4,5,6,7,8,9,10]
    even, odd = sums(lists)
    print("Odd valuse of list sum is: ", odd)
    print("Even valuse of list sum is: ", even)
