#This program is to print Nth fibonacci number

t0,t1 = 0,1

def fibon(t0,t1):
    temp= t0+t1
    t0=t1
    t1=temp
    return t0,t1

def display(num,t0,t1):
    i=0
    while True:
        print(t0," , ",t1)
        t0, t1=fibon(t0,t1)
        i=i+1
        if i>num:
            break



#main
if __name__ == "__main__":
    print(display(4,t0,t1))
