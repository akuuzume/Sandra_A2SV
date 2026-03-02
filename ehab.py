n=int(input())

arr=list(map(int,input().split()))
arr.sort(reverse=True)
for i in range(n):
    for j in range(i+1,n):
        x=arr[i]+arr[j]
        if x%2==1:
            arr[i],arr[j]=arr[j],arr[i]
print(*arr)