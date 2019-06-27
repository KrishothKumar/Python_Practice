# This program is used to Play TIC TAC TOE
import array

def play_logic(num,list,lis,n):
    if n==1:
        valus = num()
        i,j=lis[valus]
        list[i][j]="x"
        ns=2
    elif n==2:
        valus = num()
        i,j=lis[valus]
        list[i][j]="o"
        ns=1
    return list,ns

def user_input():
    valus = int(input("Enter the postion as input:\n"))
    return valus

# play_logic()
if __name__ =="__main__":
    list = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    lis= [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    count = 0
    n = 1
    while True:
        if n==1:
            list,n = play_logic(user_input,list,lis,n)
            print(list[0],end =" ")
            print("  | 0 | 1 | 2 |")
            print(list[1],end =" ")
            print("  | 3 | 4 | 5 |")
            print(list[2],end =" ")
            print("  | 6 | 7 | 8 |")
            count = count+1
            print(count,"1")

        elif n==2:
            list,n = play_logic(user_input,list,lis,n)
            print(list[0],end =" ")
            print("  | 0 | 1 | 2 |")
            print(list[1],end =" ")
            print("  | 3 | 4 | 5 |")
            print(list[2],end =" ")
            print("  | 6 | 7 | 8 |")
            count = count+1
            print(count,"2")

        elif count <= 9:
            break

        # print(play_logic(user_input,list,lis))
