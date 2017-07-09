def is_divisible(n,m):
    if n%m is 0:
        return True
    else:
        return False;
n,m=map(int,input().split())
print(is_divisible(n,m))
