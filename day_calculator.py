import datetime

def calculate_day(date1):# it has get the user date and getting day diffrence with the day
    t = datetime.date.today()
    t = t-date1

    return t

# Main statement
if __name__ =="__main__":
    date_entry = input("Enter a date in YYYY-MM-DD format: ")

    year, month, day = map(int, date_entry.split('-'))
    user_date = datetime.date(year, month, day)

    print(calculate_day(user_date))
