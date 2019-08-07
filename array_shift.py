arrs =[[0,1,2,3],
       [4,5,6,7],
       [8,9,10,11],
       [12,13,14,15]]
count =0
r = len(arrs)//2

for i in range(len(arrs)):
    for j in range(len(arrs)):
        if i == 0 or j == 0 or i == len(arrs)-1 or j == len(arrs)-1:
            if i==j or (i ==0 and j == len(arrs)-1) or (i == len(arrs)-1 and j == 0):
                temp1 = arrs[i][j]
                # arrs[i][j]= arrs[i][j+1]
                if count == 0:
                    # temp2 = arrs[i][j+1]
                    # arrs[i][j] = temp2
                    # temp1= temp2
                    print("1",i,end="")
                    print(j)
                    count = 1

                else:
                    # if i == len(arrs)-1 and j == len(arrs)-1 :
                    #     temp2 = arrs[i-1][j]
                    #     arrs[i][j] = temp2
                    #     temp1= temp2
                    # else:
                    #     temp2 = arrs[i-1][j]
                    #     arrs[i][j] = temp2
                    #     temp1= temp2

                    print("3",i,end="")
                    print(j)
                    count = 0

            else:
                print("2",i,end="")
                print(j)

print(*arrs,sep="\n")


    #
    # if i == i or j == i or i == len(arrs)-1-i or j == len(arrs)-1-i:
    #     if i==j or (i ==i and j == len(arrs)-1-i) or (i == len(arrs)-1-i and j == i):
