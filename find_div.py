# This is program is used to display Divisible of 7 and Note multiply of 5

def div_7(num,num2):
    list=[]
    for i in range(num,num2+1,1):
        if (i%7 == 0):
            list.append(i)
    return list

def mult_5(num,num2):
    ls=[]
    l= div_7(num,num2)
    for i in l:
        if (i%5 == 0):
            continue
        else:
            ls.append(i)
    return ls

#main
if __name__== "__main__":
    num = 2000
    num2 = 3200
    print(mult_5(num,num2))
