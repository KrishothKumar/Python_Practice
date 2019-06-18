# This program is used to Read file and displays count of word,sendence and character

def checking_line():
    file = []
    file = open("file.txt","r")
    count = 0
    print(type(file))
    for line in file.readlines():
        count = count+1
        print(type(line))
    print(type(line))
    file.close()
    return count

# Main
if __name__=="__main__":
    print(checking_line())
