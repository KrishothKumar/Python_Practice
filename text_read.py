# This program is used to Read file and displays count of word,sendence and character

def checking_line():
    file = open("file.txt","r")
    count = 0
    for line in file.readlines():
        count = count+1
    file.close()
    return count

# Main
if __name__=="__main__":
    print(checking_line())
