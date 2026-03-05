n,m=map(int,input().split())

arr1=list((map(int,input().split())))
arr2=list((map(int,input().split())))

j=0
ans=[]
for i in range(m):
    while j < n and arr1[j] < arr2[i]:
        j += 1
    ans.append(j)

print(*ans)