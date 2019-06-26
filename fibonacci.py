# This program is to print Nth fibonacci number

# This function is used to display the postion of values in fibonacci series
def display(user_number, t0 = 0, t1 = 1):
    iteration_stop=1
    list=[0,1]
    while True:
        # print(t0," , ",t1)
        temp= t0+t1
        t0=t1
        t1=temp
        # t0,t1 = fibon(t0,t1)
        list.append(t1)
        iteration_stop = iteration_stop+1
        if iteration_stop > user_number:
            break
    return list


# main
if __name__ == "__main__":
    user_number = int(input("Enter the number: "))
    list = display(user_number)
    print(list)
    print("Fibonacci number of",user_number,"th position in series is",list[user_number-1])
