n,t=map(int,input().split())
book=list(map(int,input().split()))

i=0
seg_time=0
count=0
while i<n and seg_time+book[i]<=t:
    seg_time+=book[i]
    count+=1
    i+=1


left=0
max_time=count
for right in range(i,n):
    seg_time+=book[right]
    count+=1

    while seg_time>t:
        seg_time-=book[left]
        count-=1
        left+=1

    max_time=max(count,max_time)
print(max_time)

