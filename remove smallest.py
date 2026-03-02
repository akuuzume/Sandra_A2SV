t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))

    if n==1:
        print("YES")
    
    elif len(set(arr))>=3:
        print("NO")
    else:
        print("YES")
    
