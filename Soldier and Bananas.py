k,n,w=input().split()

ans=[]
for i in range(1,int(w)+1):
    a= i*int(k)
    ans.append(a)
print(sum(ans)-int(n))
