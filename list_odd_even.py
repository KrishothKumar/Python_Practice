# This program is used to print odd first and even at last


def find(list):
    temp1=[]
    temp2=[]

    for i in list:
        if i%2 == 0:
            temp1.append(i)
        else:
            temp2.append(i)

    return temp2+temp1


#main
if __name__=="__main__":
    lists = [0,1,2,3,4,5,6,7,8,9,10]
    lists = find(lists)

    print(lists)
