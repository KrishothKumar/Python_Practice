# This program is to print area of Circle Radius
import math

PI =3.14

# Radius Formula for Circle Radius= Area divided by PI
def radius(area):
    radius = area/PI
    return round(math.sqrt(radius),2)

#Main Statement
if __name__ == "__main__":
    area = float(input("Enter the Area of Circle: "))
    print("Radius of the Circle is", radius(area))
