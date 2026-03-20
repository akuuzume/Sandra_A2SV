n,s=map(int,input().split())

arr=list(map(int,input().split()))

i=0
seg_sum=0
count=0
while i<n and seg_sum +arr[i]<=s:
    seg_sum+=arr[i]
    count+=1
    i+=1


max_len=count

left=0

for right in range(i,n):
    seg_sum+=arr[right]
    count+=1

    while seg_sum>s:
        seg_sum-=arr[left]
        left+=1
        count-=1
    max_len=max(max_len,count)
    
print(max_len)
    