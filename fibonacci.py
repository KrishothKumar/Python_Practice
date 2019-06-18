#This program is to print Nth fibonacci number

t0,t1 = 0,1

def fibon(t0,t1):
    temp= t0+t1
    t0=t1
    t1=temp
    return t0,t1

def display(num,t0,t1):
    i=0
    list=[0,1]
    while True:
        # print(t0," , ",t1)
        t0,t1 = fibon(t0,t1)
        list.append(t1)
        i=i+1
        if i>num:
            break
    return list


#main
if __name__ == "__main__":
    num= int(input("Enter the number: "))
    list=display(num,t0,t1)
    print("Fibonacci Series of",num,"th position in series is",list[num-1])
