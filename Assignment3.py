#here sides are A,B,C 
A=float(input("Enter first Side: "))
B=float(input("Enter second Side: "))
C=float(input("Enter third Side: "))

def is_right_angled(a,b,c):
    sides=[a,b,c]
    sides.sort()
    x=(sides[0])
    y=(sides[1])
    z=(sides[2])

    if(x**2+y**2==z**2):
        print("The triangle is right angled at Z",z)
    else:
        print("Triangle is not right angled")
is_right_angled(A,B,C)