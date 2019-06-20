# This program is used to display LCD of two numbers

from gcd import gcd

def lcd(num,num1):
    gcd_val = gcd(num,num1)
    given_mul = num*num1
    lcd_val = (given_mul//gcd_val)
    return lcd_val


# Main
if __name__=="__main__":
    print(lcd(8,16))
