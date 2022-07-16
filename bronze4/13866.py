a=list(map(int,input().split()))
res=[]
for i in range(4):
    for j in range(i+1,4):
        x=a[i]+a[j]
        y=sum(a)-x
        res.append(abs(x-y))
print(min(res))