# This program is used do calculate values like calculate
from math import sqrt,hypot,tan,cos,sin

def choise(num):
    while True:
        if num == 1:
            result = addition(user_input)
            break
        elif num == 2:
            result = subration(user_input)
            break
        elif num == 3:
            result = division(user_input)
            break
        elif num == 4:
            result = multiplication(user_input)
            break
        elif num == 5:
            result = modulo(user_input)
            break
        elif num == 6:
            result = power(user_input)
            break
        elif num == 7:
            result = square_root(user_input2)
            break
        elif num == 8:
            result = factorial(user_input2)
            break
        elif num == 9:
            result = odd_even(user_input2)
            break
        elif num == 10:
            result = trigonometric_hyp(user_input)
            break
        elif num == 11:
            result = trigonometric_tan(user_input2)
            break
        elif num == 12:
            result = trigonometric_cos(user_input2)
            break
        elif num == 13:
            result = trigonometric_sin(user_input2)
            break
        else:
            result = "No perform"
            break

    return result

def addition(adds):
    Number1, Number2 = adds()
    Number1 = Number1 + Number2
    return Number1

def subration(subs):
    Number1, Number2 = subs()
    Number1 = Number1 - Number2
    return Number1

def division(divd):
    Number1, Number2 = divd()
    Number1 = round(Number1 / Number2, 3)
    return Number1

def multiplication(mults):
    Number1, Number2 = mults()
    Number1 = Number1 * Number2
    return Number1

def modulo(mods):
    Number1, Number2 = mods()
    Number1 = Number1 % Number2
    return Number1

def power(sqrs):
    Number1, Number2 = sqrs()
    Number1 = Number1**Number2
    return Number1

def square_root(sqr_roots):
    Number1 = sqr_roots()
    return round(sqrt(Number1),3)

def factorial(facts):
    Number1 = facts()
    factor = 1

    for i in range(1,Number1+1,1):
        factor *= i
    return factor

def odd_even(oddevens):
    Number1=oddevens()
    if Number1%2 == 0:
        return "is even"
    else:
        return "is odd"
def trigonometric_hyp(hyp_fuction):
    Number1,Number2 = hyp_fuction()
    return hypot(Number1,Number2)

def trigonometric_tan(tan_fuction):
    return tan(tan_fuction())

def trigonometric_cos(cos_function):
    return cos(cos_function())

def trigonometric_sin(sin_function):
    return sin(sin_function())


def user_input():
    input_numbers = [int(input("Enter the Number1 to Calculate: ")), int(input("Enter the Number2 to Calculate: "))]
    return input_numbers

def user_input2():
    input_numbers = int(input("Enter the Number to evaluvate: "))
    return input_numbers


# Main statement
if __name__ == "__main__":

    while True:

        choose = int(input("\nChoise to perform Calculater\n1.add 2.sub 3.divd\n4.multp"
                " 5.mods 6.power\n7.sqart root 8.factorial 9.odd or even\n10.hypotenuse 11.Tan 12.Cos 13.Sin 0.End\n\n"))

        if choose > 0:

            print(choise(choose))
            continue

        elif choose == 0:

            break
