a,b=map(int, input().split())
c=int(input())
x=b+c
if x>=60:
    a=a+(x//60)
    b=x-(x//60 *60)
    if a>=24:
        a=a-24
    print(a,b)
else:
    b=x
    if a>=24:
        a=a-24
    print(a,x)