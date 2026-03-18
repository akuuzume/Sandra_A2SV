n,k=map(int,input().split())

p=list(map(int, input().split()))
p.sort()

if k==0:
    if p[0]==1:
        print(-1)
    else:
        print(p[0]-1)

elif k==n:
    print(p[-1])

else:
    x=p[k-1]
    if p[k]==x:
        print(-1)
    else:
        print(x)
