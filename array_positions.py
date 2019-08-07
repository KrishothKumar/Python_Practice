# This program is to pring sequence position of array

n=5
arr = [[col+row for col in range(n)]for row in range(n)]
val=list(input("Enter the position:"))
a , b =map(int, val)
list = [x for x in range(b,n)] + [x for x in range(0,b)]


if a == 0:

    count = 0
else:

    count = 1

for aa in arr: # This displays inti array

    print(aa)

for i in list:
    if (count == 1):
        for j in range(n-1,-1,-1):

            print(arr[j][i],",",end="")
            count = 0

    else:
        for j in range(n):

            print(arr[j][i],",",end="")
            count = 1
