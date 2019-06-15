# This program print circumference and area

PI =  3.14

def area(r):
    ar = PI * r * r
    #r*r is repesents squire and PI =3.14
    return ar


def cir(r):
    cir =  PI * 2 * r
    # 2 multiply PI=3.14 multiply r
    return cir


# Main function

if __name__ == "__main__":

    ra = float(input("Enter the Radius of Circle: "))

    print("Circumference of Circle is ", cir(ra))

    print("Area of Circle is ", area(ra))
