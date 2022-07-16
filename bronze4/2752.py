# x=list(map(int, input().split()))
# x_max=max(x)
# x_min=min(x)
#
# x.remove(x_max)
# x.remove(x_min)
#
# print(x_max,x[0],x_min)

x=list(map(int, input().split()))
x.sort()
for i in x:
    print(i,end=' ')