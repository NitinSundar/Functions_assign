def GPA(n,credit,grade):
    tot=0
    csum=0
    for i in range(n):
        tot+=credit[i]*grade[i]
        csum+=credit[i]
    total=tot/csum
    s=""
    if total<5:
        s=s+"sed_lyf"
    elif total>9:
        s=s+"GGWP"
    else:
        s=s+"normal"
    return s    
n=int(input())
credit=[]
grade=[]
credit=[int(i) for i in input().strip().split(' ')]
grade=[int(i) for i in input().strip().split(' ')]
print(GPA(n,credit,grade))
