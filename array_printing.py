# This program is used to print the valus as per the output

def print_patten(n):
    arr = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]]
    for i in range(5):
        for j in range(5):
            if i == 0 or j == 0 or i ==4 or j == 4:
                arr[i][j] = n
            elif i == 1 or i == 3 or j == 1 or j == 3:
                arr[i][j] = n-1
            elif i == 2:
                arr[i][j] = n-2
    return arr

# Main
if __name__ == "__main__":
    n= int(input("Enter the number to be print in patten:"))
    arr = print_patten(n)
    print(arr[0])
    print(arr[1])
    print(arr[2])
    print(arr[3])
    print(arr[4])
