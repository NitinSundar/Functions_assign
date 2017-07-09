from math import exp,sqrt
def yikes(x):
    k=x*exp(-1*x)
    p=sqrt(1-exp(-1*x))
    return k+p
x=int(input())
print(yikes(x))
