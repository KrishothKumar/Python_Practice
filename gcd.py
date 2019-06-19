# This program is to find the GCD(Greatest Commen Factore or Diviser)

def gcd(val,val1):

    while(val1):

        val, val1= val1, val%val1

    return val

# Main
if __name__ == "__main__":
    print("GCD of 16,24 is",gcd(16,24))
