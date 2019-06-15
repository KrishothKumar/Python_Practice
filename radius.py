# This program is to print area of Circle Radius
import math

PI =3.14

# Radius Formula for Circle Radius= Area divided by PI
def Radius(area):
    r = area/PI
    Rad=math.sqrt(r)
    #rad is Radius
    return Rad

#Main Statement
if __name__ == "__main__":
    print("Radius of the Circle is",Radius(28.26))
