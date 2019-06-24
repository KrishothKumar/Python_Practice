# This program is used to eliminate duplicate user_value

def eliminate_duplicate(lists):
    return list(set(lists))

if __name__=="__main__":
    print(eliminate_duplicate([1,2,3,3,4,2,2,5]))
