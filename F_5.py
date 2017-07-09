from random import randrange
def roll_dice(n,m):
    for i in range(m):
        k=randrange(n)
        print(k+1)
    return "That's all"
n,m=map(int,input().split())
print(roll_dice(n,m))
