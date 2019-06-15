import datetime

def get_val():
    t = datetime.datetime.now()
    hr = t.hour
    return hr

def get_nam(nam):
    return nam

def display():
    if get_val()<12:
        print("Good Morning "+ get_nam())
    elif get_val()<15:
        print("Good Afternoon " + get_nam())
    elif get_val()<19:
        print("Good Evening " + get_nam())
    else:
        print("Good Night " + get_nam())


if __name__ == "__main__":

    nams = input("Enter the Name: ")
    print(get_nam(nams))
    get_val()
