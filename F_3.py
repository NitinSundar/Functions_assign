import math
import cmath
def roots(a,b,c):
    d=b*b-4*a*c
    if d>=0:
        r1=(-b+math.sqrt(d))/2*a
        r2=(-b-math.sqrt(d))/2*a
        if d>0:
            print(str(r1)+" "+str(r2))
        else:
            print(r1)
    else:
        print("complex Roots")
        r1=(-b+cmath.sqrt(d))/2*a
        r2=(-b-cmath.sqrt(d))/2*a
        print(str(r1)+" "+str(r2))
a,b,c=map(int,input().split())
roots(a,b,c)
