
arr = [[0,1,2,3],
       [4,5,6,7],
       [8,9,10,11],
       [12,13,14,15]]

def degree_90():

        alt = [[0 for x in range(len(arr))] for x in range(len(arr))]

        for i in range(len(arr)):
            for j in range(len(arr)):

                alt[i][j] = arr[len(arr)-1-j][i]

        for a in alt:

            print(*a)


def degree_180():
    e  = 0
    alt = [[0 for x in range(len(arr))] for x in range(len(arr))]
    # alts = [[0 for x in range(len(arr))] for x in range(len(arr))]
    while True:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if e==0:
                    alt[i][j] = arr[len(arr)-1-j][i]
                else:
                    arr[i][j] = alt[len(arr)-1-j][i]
        e = e+1

        if e>2:
            break

    for a in arr:

        print(*a)

def transpose():
    alt = [[0 for x in range(len(arr))] for x in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i ==j:
                alt[i][j] = arr[j][i]
            else:
                alt[i][j] = arr[len(arr)-1-i][len(arr)-1-j]

    for a in alt:

        print(*a)

transpose()
