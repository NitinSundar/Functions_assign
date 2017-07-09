def pygLatin(st):
    s=""
    ans=""
    if st[0] is "a" or st[0] is "e" or st[0] is "o" or st[0] is "i" or st[0] is "u":
        ch=""
    else:
        ch=st[0]
    for i in range(1,len(st)):
        s=s+st[i]
    if ch=="":
        ans=ans+str(st[0])+s+"hay"
    else:
        ans=ans+s+ch+"ay"
    return ans
n=int(input())
line=[]
for i in range(n):
    line.append(list(input().split(" ")))
for i in range(n):
    print()
    for j in range(len(line[i])):
        print(pygLatin(line[i][j]),end=" ")
    
