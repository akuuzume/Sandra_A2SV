m,n=map(int,input().split())

arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))

ans=[]
for x in arr1:
    ans.append(x)

for x in arr2:
    ans.append(x)

ans.sort()
print(*ans)
