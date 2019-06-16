#This program

def largest(num):
    l = len(num)
    # print(l)
    val=0
    for i in range(0,l,1):
        if val<=num[i]:
            val=num[i]
    return val

#main
if __name__ =="__main__":
    lists = [5,11,2,3,6,4,7,8,10,9,1]
    print("The largest Number is the given list is ",largest(lists))
