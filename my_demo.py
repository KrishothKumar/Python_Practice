import datetime

def get_val():
    t = datetime.datetime.now()
    hr = t.hour
    return hr

def get_nam(nam):
    return nam

def display():
    nams = input("Enter the Name: ")
    Name=get_nam(nams)
    if get_val()<12:
        print("Good Morning "+ Name)
    elif get_val()<15:
        print("Good Afternoon " + Name)
    elif get_val()<19:
        print("Good Evening " + Name)
    else:
        print("Good Night " + Name)


if __name__ == "__main__":

    display()
