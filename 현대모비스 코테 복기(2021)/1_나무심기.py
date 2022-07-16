a=list(map(int, input().split()))
b=sorted(a)
center=((max(a)-min(a))//2)
dis=[]
for i in a:
    dis.append(abs(center-i))
print(dis)

print(a,b,center)