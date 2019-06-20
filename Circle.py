# This program print circumference and area

PI =  3.14

# r*r is repesents squire and PI =3.14
def area(r):
    return PI * (r**2)


# 2 multiply PI=3.14 multiply r
def circumference(r):
    return PI * (2 * r)


# Main
if __name__ == "__main__":
    ra = float(input("Enter the Radius of Circle: "))

    print("Circumference of Circle is ", cir(ra))
    print("Area of Circle is ", area(ra))
