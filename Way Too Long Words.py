a=int(input())

ans=[]

for _ in range(a):
    b=input().strip()
    if len(b)<=10:
        print(b)
    else :
        j=len(b)-2
        x=b[0]+str(j)+b[-1]
        ans.append(x)

for a in ans:
    print(a)
