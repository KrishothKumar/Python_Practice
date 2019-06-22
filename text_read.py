# This program is used to Read file and displays count of word,sendence and character

def checking_line(file):
    file = open(file,"r")
    count = 0
    character_count = 0
    word_count = 0

    for line in file.readlines():

        line = line.split()
        word_count += len(line)
        line_string = "".join(line)
        character_count += len(line_string)
        count = count+1

    file.close()
    return [count, word_count, character_count]


# Main
if __name__=="__main__":
    file=input("Enter the file name with extention:")
    file_count = checking_line(file)
    print("Number of lines in given file is",file_count[-3])
    print("Number of words in given file is",file_count[-2])
    print("Number of character in given file is",file_count[-1])
